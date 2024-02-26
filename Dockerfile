FROM python:3

WORKDIR /coursework

COPY ./pyproject.toml/coursework/

RUN pip install -r pyproject.toml

COPY . .