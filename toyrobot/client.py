import abc
import logging

from toyrobot.errors import InvalidCommandException
from toyrobot.parsers import Parser, CommandParser
from toyrobot.sanitizers import Sanitizer, CommandSanitizer

logger = logging.getLogger(__name__)


class Client:
    """
    Base client class, intended to host logic for the frontend of the application.
    """

    @abc.abstractmethod
    def start(self):
        """
        Starts the client.
        """
        raise NotImplementedError


class ConsoleClient(Client):
    """
    A client that consumes and produces output in and out of stdin/stdout.
    """

    def __init__(self, parser: Parser = None, sanitizer: Sanitizer = None):
        self.parser = parser if parser is not None else CommandParser()
        self.sanitizer = sanitizer if sanitizer is not None else CommandSanitizer()

    def start(self):
        """
        Continuously consumes input from stdin until an EOF or KeyboardInterrupt is detected.
        Parser output is directed to stdout.
        """
        try:
            while raw_input := input():
                commands = self.sanitizer.sanitize_raw_input(raw_input)

                for command in commands:
                    try:
                        if out := self.parser.parse(command):
                            print(out)
                    except InvalidCommandException as e:
                        logger.error(e)
        except (EOFError, KeyboardInterrupt):
            logger.info("Exiting game...")
