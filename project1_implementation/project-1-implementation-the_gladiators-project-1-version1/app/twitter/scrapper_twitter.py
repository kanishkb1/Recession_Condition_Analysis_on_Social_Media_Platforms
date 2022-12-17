import logging
import sys
import time
import warnings

import mysql.connector
import pandas as pd
import tweepy
from config import creds_sql, creds_twitter, key_word
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


"""
Auth method to connect with twitter API
CONSUMER_KEY, CONSUER_SECRET
ACCESS_TOKEN, ACCESS_TOKEN_SECRET
BARER_TOKEN are obtained from config.py
"""


def _auth_():
    global api_connect
    try:
        api_connect = tweepy.Client(
            wait_on_rate_limit=True,
            consumer_key=creds_twitter.my_consumer_key,
            consumer_secret=creds_twitter.my_consumer_secret,
            access_token=creds_twitter.my_access_token,
            access_token_secret=creds_twitter.my_access_secret,
            bearer_token=creds_twitter.my_bearer_token,
        )
        logging.warning("Connected successfully!")
    except ValueError as err:
        logging.warning(f"Error - 60: '{err}'")
    return api_connect


"""
Search method to pull recent tweets
each pull will contain max 10 tweets
"""


def _twitter_search_(api_client, sql_db):
    global search
    try:
        logging.warning("Collecting tweets...")
        search = api_client.search_recent_tweets(query=key_word.word, max_results=100)
    except ValueError as err:
        logging.warning(f"Error - 76: '{err}'")
    finally:
        try:
            search_df = pd.DataFrame()
            cursor = sql_db.cursor()
            for i in search.data:
                temp_data = pd.json_normalize(i.data, sep="_")
                search_df = search_df.append(temp_data, ignore_index=True)
            for idx, row in search_df.iterrows():
                query = "INSERT INTO twitter (tweets) VALUES (%s);"
                cursor.execute(query, (str(row.text),))
            sql_db.commit()
            cursor.close()
            logging.warning("Data inserted!")
        except ValueError as err:
            logging.warning(f"Error - 93: '{err}'")


"""
Driver code to establish connection with twitter API.
Timer is set for 2 hours delay start
After 2 hours new pull request is made with twitter API
"""


def main():
    connection_api_auth = _auth_()
    connection_sql = create_server_connection()
    while 1:
        try:
            _twitter_search_(connection_api_auth, connection_sql)
            for remaining in range(60, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write(
                    "{:2d} seconds remaining for next Twitter pull".format(remaining)
                )
                sys.stdout.flush()
                time.sleep(1)
        except ValueError as err:
            logging.warning(f"Error - 115: '{err}'")


if __name__ == "__main__":
    main()
