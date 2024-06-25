from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from toyrobot.errors import SouthOutOfBoundException, NorthOutOfBoundException, \
    WestOutOfBoundException, EastOutOfBoundException, InvalidPlacementException


class Direction(str, Enum):
    NORTH = "NORTH"
    EAST = "EAST"
    WEST = "WEST"
    SOUTH = "SOUTH"

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class Coordinates:
    x: int
    y: int
    f: Direction


class Robot:
    def __init__(self, direction=Direction.NORTH):
        self.direction = direction

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
        """
        Places a given robot into the board within the given coordinates.
        """
        if x >= self.cols or y >= self.rows:
            raise InvalidPlacementException

        self.reset()
        robot.direction = f
        self.squares[y * self.cols + x] = robot

    def reset(self):
        """
        Reset's the board to its initial empty state.
        """
        self.squares: List[Optional[Robot]] = [None for _ in range(self.rows * self.cols)]

    def report(self) -> Optional[Coordinates]:
        """
        Returns the coordinate of the first robot found.
        """
        for i, square in enumerate(self.squares):
            if square is not None:
                x = i % self.cols
                y = (i - x) // self.cols
                return Coordinates(x, y, square.direction)

    def move(self, robot: Robot):
        """
        Moves the given robot one square forward the direction it's facing.
        If the robot hasn't been placed yet, this method has no effect.
        """
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
        """
        Determines how many steps backward/forward a direction goes with respect to the board being a 1D list.
        """
        match direction:
            case Direction.WEST:
                return -1
            case Direction.EAST:
                return 1
            case Direction.SOUTH:
                return -self.cols
            case Direction.NORTH:
                return self.cols
