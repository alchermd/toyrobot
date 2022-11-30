import logging

from toyrobot.client import ConsoleClient

logging.disable(logging.CRITICAL)


def main():
    client = ConsoleClient()
    client.start()


if __name__ == "__main__":
    main()
