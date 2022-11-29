# toyrobot

J.A. Doloiras' submission for the Toy Robot Code Challenge as part of his application for iress.

## Usage (with Docker)

```console
$ docker build -t toyrobot:latest .
$ docker run toyrobot
```

The test suite can be ran via `docker run toyrobot python runtests.py`

## Usage (without Docker)

```console
$ python3 --version 
Python 3.10.8
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

The test suite can be ran via `python runtests.py`