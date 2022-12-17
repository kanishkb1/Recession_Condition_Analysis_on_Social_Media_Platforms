import sys
import time

import mysql.connector
from config.config import creds_nyt, creds_sql
from mysql.connector import Error
import logging
import warnings
import requests
import json

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
        logging.warning(f"Error - 34: '{err}'")

    return connect_sql


def scrap_nyt():
    NYTimes_API_KEY = creds_nyt.API_KEY
    NYTimes_Search_URL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q={0}+&api-key=' + NYTimes_API_KEY
    r = requests.get(NYTimes_Search_URL.format(creds_nyt.topic))
    data = json.loads(r.text)
    # print(type(data))
    return data['response']['docs']


def store_data_sql(data, sql_db):
    try:
        cursor = sql_db.cursor()
        for idx in data:
            query = "INSERT INTO nyt (PullDate, text) VALUES (now(), %s);"
            cursor.execute(query, (str(idx['abstract']),))
        sql_db.commit()
        cursor.close()
        logging.warning("Data inserted!")
    except ValueError as err:
        logging.warning(f"Error - 93: '{err}'")


def main():
    sql_auth = create_server_connection()
    while 1:
        try:
            data = scrap_nyt()
            store_data_sql(data, sql_auth)
            for remaining in range(60, 0, -1):
                # sys.stdout.write("\r")
                # sys.stdout.write(
                #     "{:2d} seconds remaining for next NY Times pull".format(remaining)
                # )
                # sys.stdout.flush()
                time.sleep(1)
        except ValueError as err:
            logging.warning(f"Error - 94: '{err}'")


if __name__ == "__main__":
    main()
