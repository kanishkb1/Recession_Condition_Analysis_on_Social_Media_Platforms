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

## Intro

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions

## Project Structure

    .
    ├── ...
    ├── data                    
    │   ├── twitter.csv        
    │   ├── reddit.csv         
    │   └── nyt.csv          
    ├── static
    │   ├── images 
    │   ├── style.css       
    │   └── ...
    ├── templates
    │   ├── index.html    
    │   ├── ...
    ├── core
    │   ├── config.py
    ├── main.py
    └── ...

## Build

Building env: Installing [poetry](https://python-poetry.org/) and setting up virtiual environment.

```
$ sh build.sh
```


## Run

Start flask server on default port

```
$ sh run.sh
```


# Linter

Lint, or a linter, is a static code analysis tool used to flag programming errors, bugs, stylistic errors and suspicious constructs.

> _Linter using poetry env_

```
$ poetry run isort .
$ poetry run black .
$ poetry run flake8
```


#### References 

[1] Flask Library Documentation.
https://flask.palletsprojects.com/

[2] WordCloud Library Documentation.
https://pypi.org/project/wordcloud

[3] Seaborm Library Documentation. 
https://seaborn.pydata.org/

[4] Matplotlib Library Documentation
https://matplotlib.org/

[5] Textblob Library Documentation.
https://textblob.readthedocs.io/en/dev/



