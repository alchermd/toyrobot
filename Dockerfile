FROM python:3.10-slim-buster

WORKDIR /opt/toyrobot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]