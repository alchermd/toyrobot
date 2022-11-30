import logging
import re

from toyrobot.errors import OutOfBoundMovementException, UnparsableCommandException, InvalidCommandException
from toyrobot.models import Board, Robot, Coordinates

logger = logging.getLogger(__file__)


class Parser:
    def parse(self, command: str):
        raise NotImplementedError


class CommandParser(Parser):
    def __init__(self, board: Board = None, robot: Robot = None):
        self.board = board if board is not None else Board()
        self.robot = robot if robot is not None else Robot()

        self.commands = []

    def parse(self, command: str):
        if match := re.search(r"PLACE (\d),(\d),(NORTH|EAST|WEST|SOUTH|N|E|W|S)", command):
            x = int(match.group(1))
            y = int(match.group(2))
            f = match.group(3)

            match f:
                case "N":
                    f = "NORTH"
                case "E":
                    f = "EAST"
                case "W":
                    f = "WEST"
                case "S":
                    f = "SOUTH"

            self.commands.append(match.group())
            return self.board.place(self.robot, x, y, f)
        elif not self.place_command_executed:
            raise InvalidCommandException

        if command == "REPORT":
            coordinates = self.board.report()
            return self.parse_coordinates(coordinates)
        elif command == "MOVE":
            try:
                return self.board.move(self.robot)
            except OutOfBoundMovementException as e:
                logger.error(e)
        elif command == "LEFT":
            return self.robot.turn_left()
        elif command == "RIGHT":
            return self.robot.turn_right()

        raise UnparsableCommandException

    @staticmethod
    def parse_coordinates(coordinates: Coordinates) -> str:
        return f"Output: {coordinates.x},{coordinates.y},{coordinates.f}"

    @property
    def place_command_executed(self) -> bool:
        return bool(list(filter(lambda command: command.startswith("PLACE"), self.commands)))
