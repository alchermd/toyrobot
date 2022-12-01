# toyrobot

![](./notes/toyrobot.gif)

J.A. Doloiras' submission for the Toy Robot Code Challenge as part of his application for iress.

## Setup (with Docker)

```console
$ docker build -t toyrobot:latest .
$ docker run -it toyrobot
```

The test suite can be run via `docker run toyrobot python runtests.py`

## Setup (without Docker)

```console
$ python3 --version 
Python 3.10.8
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```

The test suite can be ran via `python runtests.py`

## Usage

Running the `main.py` script will start the app in interactive mode. An example `infile` containing the test commands
from the instruction PDF is provided. It that can be piped to the main script. For example:

```console
$ cat infile | python main.py > outfile
$ docker run toyrobot cat infile | python main.py > outfile && cat outfile # if using docker
```

For supported commands, please enter `HELP` on the interactive terminal.

## Architecture

![](./notes/images/architecture.png)

## Notes

Included in the repo is a `notes` directory, containing my thoughts in a "braindump" format that I usually take while I
tackle on a new feature/project.