FROM python:3

WORKDIR /coursework

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install bash python3 python3-dev postgresql-client  && \
    rm -vrf /var/cache/apk/* && \
    curl -sSL https://install.python-poetry.org  | python - && \
    poetry config virtualenvs.create false --local

COPY poetry.lock .

COPY pyproject.toml .

RUN poetry install

COPY . .
