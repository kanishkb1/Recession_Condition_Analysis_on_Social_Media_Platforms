import json
import os
import os.path
from datetime import date, timedelta

import matplotlib.pyplot as plt
from flask import Flask, redirect, render_template, request
from textblob import TextBlob
from wordcloud import STOPWORDS, WordCloud

from core.config import loadDataFrames

# Absolute paths for graphs
graphsPath = [
    "/static/images/wfplot.png",
    "/static/images/wcplot.png",
    "static/images/saplot.png",
    "static/images/mugraph.png",
]

# Create local dataframes obj
dft, dfr, dfn = loadDataFrames()

app = Flask(__name__)


# Logger for flask
# logging.basicConfig(level=logging.DEBUG)


def getEndDate(delta):
    startDate = date(2022, 11, 1)
    difference = timedelta(days=delta)
    dd = startDate + difference
    endDate = str(dd.strftime("%Y-%m-%-d"))
    return endDate


def createDataFrame(delta, dataframe):
    endDate = getEndDate(delta)
    print("Creating data from 2022-11-04 to ", endDate)
    df = (dataframe["PullDate"] >= "2022-11-01") & (dataframe["PullDate"] <= endDate)
    newdf = dataframe.loc[df]
    return newdf


def generateGraphs(delta, df):
    # Create new dataframe according to selected range
    dataframe = createDataFrame(delta, df)
    # Word Cloud graph
    plotWordCloud(dataframe)
    # Word Frequency graph
    plotWordFrequency(dataframe["text"])
    # Sentimental Analysis
    sentimentalScore(dataframe["text"])


def sentimentalScore(text):
    def classification(text):
        return TextBlob(text).sentiment.polarity
    polarity_score = text.apply(lambda x : classification(x))
    plt.xlabel('Score range ')
    plt.ylabel('Number of occurences')
    plt.title('Sentimental Analysis Score')
    ax = polarity_score.hist()
    for bar in ax.containers[0]:
      x = bar.get_x() + 0.5 * bar.get_width()
      if x > 0.12:
        bar.set_color('green')
      elif x<-0.12:
        bar.set_color('red')
      else:
        bar.set_color('blue')
    if os.path.exists("static/images/saplot.png"):
        os.remove(f"static/images/saplot.png")
    plt.savefig("static/images/saplot.png")


def plotWordFrequency(text):
    print("Plotting new graph")
    plt.figure(figsize=(8, 8))
    plt.xlabel("Word Length")
    plt.ylabel("Number of occurrences")
    plt.title("Word Frequency Graph")
    plt.grid(True)
    text.str.split().map(lambda x: len(x)).hist()
    if os.path.exists("static/images/wfplot.png"):
        os.remove(f"static/images/wfplot.png")
    plt.savefig("static/images/wfplot.png")


def plotWordCloud(df):
    df = df.astype(str)
    review_words = " "
    for i in df.text:
        i = str(i)
        separate = i.split()
        for j in range(len(separate)):
            separate[j] = separate[j].lower()
        review_words += " ".join(separate) + " "
    stop_words = set(STOPWORDS)
    final_wordcloud = WordCloud(
        width=800,
        height=800,
        background_color="white",
        stopwords=stop_words,
        min_font_size=4,
    ).generate(review_words)
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(final_wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    if os.path.exists("static/images/wcplot.png"):
        os.remove(f"static/images/wcplot.png")
    plt.savefig("static/images/wcplot.png")


@app.route("/")
def index():
    # unitTest()
    return render_template("index.html")


# Twitter page driver function
@app.route("/twittergraphs", methods=["POST"])
def twittergraphs():
    output = request.get_json()
    result = json.loads(output)
    days = int(result["valDays"])
    print("Days: ", days)
    generateGraphs(days, dft)
    print("Graphs plotted, need manual refresh...")
    return redirect(request.referrer)


@app.route("/redditgraphs", methods=["POST"])
def redditgraphs():
    output = request.get_json()
    result = json.loads(output)
    days = int(result["valDays"])
    print("Days: ", days)
    generateGraphs(days, dfr)
    print("Graphs plotted, need manual refresh...")
    return redirect(request.referrer)


@app.route("/nytgraphs", methods=["POST"])
def nytgraphs():
    output = request.get_json()
    result = json.loads(output)
    days = int(result["valDays"])
    print("Days: ", days)
    generateGraphs(days, dfn)
    print("Graphs plotted, need manual refresh...")
    return redirect(request.referrer)


# Unit testing function
# def unitTest():
#     days = 60
#     print("Generating graph for twitter dataset with range ", days)
#     generateGraphs(days, dft)

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
