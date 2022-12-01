import logging
import re

from toyrobot.errors import OutOfBoundMovementException, UnparsableCommandException, InvalidCommandException, \
    InvalidPlacementException
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
        self.help_text = """
PLACE x,y,f
    Places the robot in the x,y coordinate while facing the f direction. 
    x and y must fall between 0-4.
    f must be one of the following values: NORTH, N, EAST, E, WEST, W, SOUTH, S 
    
MOVE
    Moves the robot one space towards the direction it's facing. 
    Move commands that makes the robot fall out of the table are ignored.
    
LEFT
    Rotates the robot 90 degrees to its left, relative to the direction it's facing.
    
RIGHT
    Rotates the robot 90 degrees to its right, relative to the direction it's facing. 
    
REPORT
    Display's the robot's current coordinates and the direction it's facing.
    
EXIT
    Quits the application. 
    Detecting EOF from the input stream will quit the application.
    A keyboard interrupt (CTRL+D / CTRL+C) will also quit the application.
    
HELP
    Shows the available commands.
    
Commands are case-insensitive. Unknown and invalid commands are ignored.

---

"""

    def parse(self, command: str):
        if match := re.search(r"PLACE (\d+),(\d+),(NORTH|EAST|WEST|SOUTH|N|E|W|S)", command):
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
            try:
                self.commands.append(match.group())
                return self.board.place(self.robot, x, y, f)
            except InvalidPlacementException:
                raise InvalidCommandException
        elif command == "EXIT":
            raise EOFError
        elif command == "HELP":
            return self.help_text
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
