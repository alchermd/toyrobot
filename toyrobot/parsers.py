import logging
import re

from toyrobot.errors import OutOfBoundMovementException
from toyrobot.models import Board, Robot, Coordinates

logger = logging.getLogger(__file__)


class Parser:
    def parse(self, command: str):
        raise NotImplementedError


class CommandParser(Parser):
    def __init__(self, board: Board = None, robot: Robot = None):
        self.board = board if board is not None else Board()
        self.robot = robot if robot is not None else Robot()

    def parse(self, command: str):
        if command == "REPORT":
            coordinates = self.board.report()
            return self.parse_coordinates(coordinates)
        elif command == "MOVE":
            try:
                self.board.move(self.robot)
            except OutOfBoundMovementException as e:
                logger.error(e)
        elif command == "LEFT":
            self.robot.turn_left()
        elif command == "RIGHT":
            self.robot.turn_right()
        elif match := re.search(r"PLACE (\d),(\d),(NORTH|EAST|WEST|SOUTH|N|E|W|S)", command):
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

            self.board.place(self.robot, x, y, f)
        else:
            return ""

    @staticmethod
    def parse_coordinates(coordinates: Coordinates):
        return f"Output: {coordinates.x},{coordinates.y},{coordinates.f}"
