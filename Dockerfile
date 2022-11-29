FROM python:3.10-slim-buster

WORKDIR /opt/toyrobot

COPY . .

CMD ["python", "main.py"]