#!/bin/bash


################################
# Install dependency
################################
# Poetry version 1.1.11
#
# Setup virtual env
################################
if ! [ -x "$(command -v poetry)" ]; then
  echo "#####################################"
  echo "#"
  echo "# Installing poetry and setting env #"
  echo "#"
  echo "#####################################"
  python get-pip.py
  pip install --no-cache-dir poetry==1.1.11
  poetry config virtualenvs.create false
  poetry install --no-interaction --no-ansi

else
################################
# Run scrapper
################################
# Twitter API
#
# Reddit API
#
# New York Times API
################################
  echo "####################"
  echo "#"
  echo "# Running scrapper #"
  echo "#"
  echo "####################"
#  python3 app/counter.py &
  python3 app/twitter/twitter.py &
  python3 app/reddit/scrapper_reddit.py &
  python3 app/nyt/scrapper_nyt.py &
  cd ui/
  uvicorn main:app
fi
