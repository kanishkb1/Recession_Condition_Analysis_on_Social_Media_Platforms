import fastapi
import fastapi.responses as _responses
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error

router = fastapi.APIRouter()
FILE_NAME = "result.png"
connect = None
try:
    connect = mysql.connector.connect(
        host="localhost",
        user="root",
        port=3303,
        passwd="admin123456",
    )
    print("MySQL Database connection successful")
except Error as err:
    print(f"Error - 34: '{err}'")


@router.post("/api", responses={})
async def twitter_graph():
    try:
        c = connect.cursor()
        sql = "SELECT count(*) FROM dsp_tweets.twitter;"
        c.execute(sql)
        res = c.fetchone()
        r = int(res[0])

        xgraphArray = [0, r]
        ygraphArray = [0, 14]

        plt.plot(xgraphArray, ygraphArray)
        plt.title("Scrapping of data")
        plt.xlabel("No of tweets")
        plt.ylabel("Date")
        plt.savefig("result.png")
    except ValueError as err:
        print(f"Error - 43: '{err}'")
        print(f"Error - 40: '{err}'")

    return _responses.FileResponse(FILE_NAME)
