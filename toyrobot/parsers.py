import re

from toyrobot.models import Board, Robot, Coordinates


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
    def parse_coordinates(coordinates: Coordinates):
        return f"Output: {coordinates.x},{coordinates.y},{coordinates.f}"
