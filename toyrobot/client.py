from toyrobot.parsers import Parser, CommandParser
from toyrobot.sanitizers import Sanitizer, CommandSanitizer


class Client:
    def start(self):
        raise NotImplementedError


class ConsoleClient(Client):
    def __init__(self, parser: Parser = None, sanitizer: Sanitizer = None):
        self.parser = parser if parser is not None else CommandParser()
        self.sanitizer = sanitizer if sanitizer is not None else CommandSanitizer()

    def start(self):
        raw_input = input(">>> ")
        commands = self.sanitizer.sanitize_raw_input(raw_input)

        for command in commands:
            if out := self.parser.parse(command):
                print(out)
