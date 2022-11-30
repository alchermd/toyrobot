from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from toyrobot.errors import SouthOutOfBoundException, NorthOutOfBoundException, \
    WestOutOfBoundException, EastOutOfBoundException


class Direction(str, Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    WEST = "WEST"
    SOUTH = "SOUTH"


@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int
    f: Direction


class Robot:
    def __init__(self):
        self.direction = Direction.NORTH

    def turn_left(self):
        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.WEST
            case Direction.EAST:
                self.direction = Direction.NORTH
            case Direction.WEST:
                self.direction = Direction.SOUTH
            case Direction.SOUTH:
                self.direction = Direction.EAST

    def turn_right(self):
        match self.direction:
            case Direction.NORTH:
                self.direction = Direction.EAST
            case Direction.EAST:
                self.direction = Direction.SOUTH
            case Direction.WEST:
                self.direction = Direction.NORTH
            case Direction.SOUTH:
                self.direction = Direction.WEST


class Board:
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols
        # Initially empty list of nullable robots
        self.squares: List[Optional[Robot]] = [None for _ in range(rows * cols)]

    def place(self, robot: Robot, x: int, y: int, f: Direction):
        robot.direction = f
        self.squares[y * self.cols + x] = robot

    def report(self) -> Coordinates:
        for i, square in enumerate(self.squares):
            if square is not None:
                x = i % self.cols
                y = (i - x) // self.cols
                return Coordinates(x, y, square.direction)

    def move(self, robot: Robot):
        for current_index, square in enumerate(self.squares):
            if square is robot:
                target_index = current_index + self._get_offset(robot.direction)
                if robot.direction == Direction.SOUTH and target_index < 0:
                    raise SouthOutOfBoundException

                if robot.direction == Direction.NORTH and target_index >= len(self.squares):
                    raise NorthOutOfBoundException

                if robot.direction == Direction.WEST and current_index % self.cols == 0:
                    raise WestOutOfBoundException

                if robot.direction == Direction.EAST and (current_index + 1) % self.cols == 0:
                    raise EastOutOfBoundException

                self.squares[current_index] = None
                self.squares[target_index] = robot
                break

    def _get_offset(self, direction: Direction) -> int:
        match direction:
            case Direction.WEST:
                return -1
            case Direction.EAST:
                return 1
            case Direction.SOUTH:
                return -self.cols
            case Direction.NORTH:
                return self.cols
