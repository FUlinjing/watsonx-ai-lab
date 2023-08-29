FROM python:3.10-slim-bullseye

RUN apt-get update && apt-get install dnsutils iputils-ping curl -y
RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT python3 app.py

