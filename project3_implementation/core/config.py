import pandas as pd


def loadDataFrames():
    print("Loading dataset from CSV to dataframes...")
    dataframeTwitter = pd.read_csv("data/twitter.csv")
    dataframeTwitter["PullDate"] = pd.to_datetime(dataframeTwitter["PullDate"])
    dataframeReddit = pd.read_csv("data/reddit.csv")
    dataframeReddit["PullDate"] = pd.to_datetime(dataframeReddit["PullDate"])
    dataframeNYT = pd.read_csv("data/nyt.csv")
    dataframeNYT["PullDate"] = pd.to_datetime(dataframeNYT["PullDate"])

    return dataframeTwitter, dataframeReddit, dataframeNYT
