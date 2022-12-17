import json
import logging
import warnings
import sys

import mysql.connector
import requests
from config import creds_sql, creds_twitter
from mysql.connector import Error

# This sets the root logger to write to stdout (your console).
logging.basicConfig()
warnings.filterwarnings("ignore")


def create_server_connection():
    connect_sql = None
    try:
        connect_sql = mysql.connector.connect(
            host=creds_sql.host,
            user=creds_sql.username,
            port=creds_sql.port,
            passwd=creds_sql.password,
            database=creds_sql.database,
        )
        logging.warning("MySQL Database connection successful")
    except Error as err:
        logging.warning(f"Error - 27: '{err}'")

    return connect_sql


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {creds_twitter.my_bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "rescission", "tag": "rescission"},
        {"value": "layoff", "tag": "layoff"},
        {"value": "employees fired", "tag": "employees fired"},
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(sql):
    try:
        response = requests.get(
            "https://api.twitter.com/2/tweets/search/stream",
            auth=bearer_oauth,
            stream=True,
        )
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Cannot get stream (HTTP {}): {}".format(
                    response.status_code, response.text
                )
            )
        i = 0
        cursor = sql.cursor()
        for response_line in response.iter_lines():
            if response_line:
                i = i + 1
                json_response = json.loads(response_line)
                text = str(json_response["data"]["text"])
                if 'RT' not in text[0:3]:
                    try:
                        query = (
                            "INSERT INTO twitter (PullDate, text) VALUES (now(), %s);"
                        )
                        cursor.execute(query, (text,))
                        sql.commit()
                        # logging.warning("Data inserted!")
                        sys.stdout.write("\r")
                        sys.stdout.write(
                            "{:2d} tweets data inserted!".format(i)
                        )
                        sys.stdout.flush()
                    except ValueError as err:
                        logging.warning(f"Error - 121: '{err}'")
        cursor.close()
    except ValueError as err:
        logging.warning(f"Error - 133: '{err}'")


def main():
    rules = get_rules()
    sql = create_server_connection()
    delete = delete_all_rules(rules)
    set_rules(delete)
    get_stream(sql)


if __name__ == "__main__":
    main()
