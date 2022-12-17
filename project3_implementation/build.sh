#!/bin/bash


################################
# Install dependency
################################
# Poetry version 1.1.11
#
# Setup virtual env
################################
  echo "#####################################"
  echo "#"
  echo "# Installing poetry and setting env #"
  echo "#"
  echo "#####################################"
  python get-pip.py
  pip install --no-cache-dir poetry==1.1.11
  poetry config virtualenvs.create false
  poetry install --no-interaction --no-ansi
