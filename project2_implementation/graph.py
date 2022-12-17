import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
import pandas as pd
from sqlalchemy import create_engine
import datetime as dt
import matplotlib.dates as mdates


db_connection_str = 'mysql+pymysql://root:admin123456@localhost/dsp_reddit'
db_connection = create_engine(db_connection_str)


def graphy():
    try:
        query = """SELECT DATE(`reddit_politics`.`Pulldate`) AS `date`, COUNT(`reddit_politics`.`id`) AS `count` FROM `reddit_politics` 
        WHERE `reddit_politics`.`PullDate` BETWEEN '2022-11-01' AND '2022-11-22' GROUP BY `date` ORDER BY `date`;"""
        df = pd.read_sql(query, con=db_connection)
        plt.xlabel("Dates")
        plt.ylabel("Number of subreddit r/Politics comments")
        plt.figure(figsize=(10, 10))
        plt.plot(df["date"], df["count"],'-o')
        plt.savefig("reddit_politics3.png")
        print('Graph ready')
        

    except ValueError as err:
        print(f"Error - 43: '{err}'")

graphy()
