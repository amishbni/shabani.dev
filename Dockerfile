FROM python:3.9.7-alpine

RUN pip install pip --upgrade
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

