# Social Media Data Science Pipeline (CS 515)

![bu](.img/bulogo.png)

## Project-2 Implementation

### Group 
> _the_gladiators_

### Team Members
- Nikita Mandlik (nmandli1@binghamton.edu)
- Brinda Eshwar (beshwar1@binghamton.edu)
- Kanishk Bharampurkar (kbarhan1@binghamton.edu)
- Harshad Bhandwaldar (hbhandw1@binghamton.edu)

### Introduction

The  data collected using the RedditAPI, will be used to study and develop insights about the public opinion on politics and the influence of upcoming-politics updates.

### Data Sources
- Reddit API

### How to use?

- Scrapper: app folder has reddit api to scrape data and store it in database.
- UI: Using fastapi data can be visualized. The api function only has functionality to display the database data.

#### Building and running application

Building env: Installing [poetry](https://python-poetry.org/) and setting up virtiual environment.
```
$ sh build.sh
```

### Running in debug mode

Running application:
```
$ python3 /app/reddit/scrapper_reddit_politics.py
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

[1] Reddit API Documentation. https://www.reddit.com/dev/api/

[2] Docker Documentation. https://docs.docker.com/get-started/overview/

[3] Poetry Documentation. https://python-poetry.org/docs/

[4] MySQL Documentation. https://dev.mysql.com/doc/