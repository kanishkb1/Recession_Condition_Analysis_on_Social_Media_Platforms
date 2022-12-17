# Pull base image
FROM python:3.9

# Create work directory
WORKDIR /usr/src/scrap

#Install poetry env, project dependency and model files
COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir poetry==1.1.11 && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

#Copy files
COPY ./ ./
RUN chmod +x /usr/src/scrap/build.sh

#Expose port and run application
ENTRYPOINT ["/bin/sh", "/usr/src/scrap/build.sh"]