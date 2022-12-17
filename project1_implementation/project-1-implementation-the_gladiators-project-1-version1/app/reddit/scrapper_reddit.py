import logging
import sys
import time
import warnings
from datetime import datetime

import mysql.connector
import pandas as pd
import requests
from config.config import creds_reddit, creds_sql
from mysql.connector import Error

# This sets the root logger to write to stdout (your console).
logging.basicConfig()
warnings.filterwarnings("ignore")

"""
Method to establish SQL connection
SQL connection details are passed from config
"""


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
        logging.warning(f"Error - 34: '{err}'")

    return connect_sql


# we use this function to convert responses to dataframes
def df_from_response(res):
    # initialize temp dataframe for batch of data in response
    df = pd.DataFrame()

    # loop through each post pulled from res and append to df
    for post in res.json()["data"]["children"]:
        df = df.append(
            {
                "subreddit": post["data"]["subreddit"],
                "title": post["data"]["title"],
                "selftext": post["data"]["selftext"],
                "upvote_ratio": post["data"]["upvote_ratio"],
                "ups": post["data"]["ups"],
                "downs": post["data"]["downs"],
                "score": post["data"]["score"],
                "link_flair_css_class": post["data"]["link_flair_css_class"],
                "created_utc": datetime.fromtimestamp(
                    post["data"]["created_utc"]
                ).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "id": post["data"]["id"],
                "kind": post["kind"],
            },
            ignore_index=True,
        )

    return df


def auth_api():
    # authenticate API
    client_auth = requests.auth.HTTPBasicAuth(
        "qY1xfxRVZb1qA9pYLUDrWg", "n_77Mf8ESzu948iyK9qv3rYJL9Q9_w"
    )
    data = {
        "grant_type": "password",
        "username": creds_reddit.username,
        "password": creds_reddit.password,
    }
    headers = {"User-Agent": "app1/0.0.1"}
    # send authentication request for OAuth token
    res = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=client_auth,
        data=data,
        headers=headers,
    )
    # extract token from response and format correctly
    token = f"bearer {res.json()['access_token']}"
    # update API headers with authorization (bearer token)
    headers = {**headers, **{"Authorization": token}}
    return headers


def scrap_reddit(headers, sql_db):
    try:
        # initialize dataframe and parameters for pulling data in loop
        data = pd.DataFrame()
        params = {"limit": 100}
        for i in range(3):
            res = requests.get(
                "https://oauth.reddit.com/r/recession/new",
                headers=headers,
                params=params,
            )
            new_df = df_from_response(res)
            data = data.append(new_df, ignore_index=True)
        # for ind in data.index:
        #     print(data["title"][ind], " \n ")
    except ValueError as err:
        logging.warning(f"Error - 106: '{err}'")
    finally:
        try:
            cursor = sql_db.cursor()
            for idx in data.index:
                query = "INSERT INTO reddit (PullDate, text) VALUES (now(), %s);"
                cursor.execute(query, (str(data["title"][idx]),))
            sql_db.commit()
            cursor.close()
            # logging.warning("Data inserted!")
        except ValueError as err:
            logging.warning(f"Error - 93: '{err}'")


def main():
    headers = auth_api()
    sql_auth = create_server_connection()
    while 1:
        try:
            scrap_reddit(headers, sql_auth)
            for remaining in range(60, 0, -1):
                # sys.stdout.write("\r")
                # sys.stdout.write(
                #     "{:2d} seconds remaining for next Reddit pull".format(remaining)
                # )
                # sys.stdout.flush()
                time.sleep(1)
        except ValueError as err:
            logging.warning(f"Error - 94: '{err}'")


if __name__ == "__main__":
    main()
