import re
from typing import List

from toyrobot.models import Board, Robot, Coordinates


class Client:
    pass


class ConsoleClient(Client):
    def __init__(self):
        self.board = Board()
        self.robot = Robot()

    def start(self):
        raw_input = input(">>> ")
        commands = self._sanitize_input(raw_input)

        for command in commands:
            if out := self._parse_command(command):
                print(out)

    def _parse_command(self, command: str) -> str:
        if command == "REPORT":
            coordinates = self.board.report()
            return self._parse_coordinates(coordinates)
        elif command == "MOVE":
            self.board.move(self.robot)
        elif command == "LEFT":
            self.robot.turn_left()
        elif command == "RIGHT":
            self.robot.turn_right()
        elif match := re.search(r"PLACE (\d),(\d),(NORTH|EAST|WEST|SOUTH)", command):
            x = int(match.group(1))
            y = int(match.group(2))
            f = match.group(3)

            self.board.place(self.robot, x, y, f)
        else:
            return ""

    @staticmethod
    def _parse_coordinates(coordinates: Coordinates) -> str:
        return f"Output: {coordinates.x},{coordinates.y},{coordinates.f}"

    @staticmethod
    def _sanitize_input(raw_input: str) -> List[str]:
        return [command.strip().upper() for command in raw_input.split("\n")]
