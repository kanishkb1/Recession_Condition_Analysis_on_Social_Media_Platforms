# Social Media Data Science Pipeline (CS 515)

![bu](.img/bulogo.png)

## Project-1 Implementation

### Group 
> _the_gladiators_

### Team Members
- Nikita Mandlik (nmandli1@binghamton.edu)
- Brinda Eshwar (beshwar1@binghamton.edu)
- Kanishk Bharampurkar (kbarhan1@binghamton.edu)
- Harshad Bhandwaldar (hbhandw1@binghamton.edu)

### Introduction

The  data collected using the Twitter API and the RedditAPI, will be used to study and develop insights about the public opinion on the economic crisis, inflation, and the influence of upcoming-recession updates. The data will help to predict the impact of the upcoming recession on the community. Also, to analyze the insights generated from the public opinionated datasets (Reddit and Twitter) and news articles (collected from NewYork Times API).

### Data Flow Diagram 

![ ](.img/DataFlowDiagram.png "Data Flow Diagram")

### Data Sources
- Twitter API
- Reddit API
- New York Times API

### How to use?

- Scrapper: app folder has twitter, reddit and ny times api to scrape data and store it in database.
- UI: Using fastapi data can be visualize. The api function only has functionality to display the database data.

#### Building application

Building env: Installing [poetry](https://python-poetry.org/) and setting up virtiual environment.
```
$ sh build.sh
```

Running application (run each scrapper independently):
```
$ python3 /app/twitter/scrapper_twitter.py
$ python3 /app/reddit/scrapper_reddit.py
$ python3 /app/nyt/scrapper_nyt.py
```

Running UI:
```
cd ui/
$ uvicorn main:app --reload
```
Go to http://localhost:8000/docs to open UI.

#### Configuration

API keys and database credentials changed from config.py located at root of each app.

### System requirement

| Name | Requirement |
| ------ | ------ |
| Memory | 8Gb |
| OS | Linux |

#### References 

[1] Twitter API Documentation. https://developer.twitter.com/en/docs/twitter-api

[2] Reddit API Documentation. https://www.reddit.com/dev/api/

[3] NYTimes API Documentation. https://developer.nytimes.com/apis

[4] Article Search API Documentation.  https://developer.nytimes.com/docs/articlesearch-product/1/overview

[5] Docker Documentation. https://docs.docker.com/get-started/overview/

[6] Poetry Documentation. https://python-poetry.org/docs/

[7] MySQL Documentation. https://dev.mysql.com/doc/
