import unittest
from typing import Tuple, List

from toyrobot.errors import SouthOutOfBoundException, WestOutOfBoundException, EastOutOfBoundException, \
    NorthOutOfBoundException, OutOfBoundMovementException
from toyrobot.models import Board, Robot, Direction, Coordinates


class PlacementAndMovementTestCase(unittest.TestCase):
    def test_can_place_the_robot_in_the_board_and_report_its_location(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.NORTH)
        self.assertEqual(Coordinates(2, 2, Direction.NORTH), board.report())

    def test_can_move_the_robot_north_and_report_its_updated_location(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.NORTH)
        board.move(robot)
        self.assertEqual(Coordinates(2, 3, Direction.NORTH), board.report())

    def test_can_move_the_robot_east_and_report_its_updated_location(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.EAST)
        board.move(robot)
        self.assertEqual(Coordinates(3, 2, Direction.EAST), board.report())

    def test_can_move_the_robot_west_and_report_its_updated_location(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.WEST)
        board.move(robot)
        self.assertEqual(Coordinates(1, 2, Direction.WEST), board.report())

    def test_can_move_the_robot_south_and_report_its_updated_location(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.SOUTH)
        board.move(robot)
        self.assertEqual(Coordinates(2, 1, Direction.SOUTH), board.report())

    def test_placing_and_reporting_works_with_custom_dimensions(self):
        board = Board(rows=4, cols=2)
        robot = Robot()
        board.place(robot, x=1, y=1, f=Direction.SOUTH)
        self.assertEqual(Coordinates(1, 1, Direction.SOUTH), board.report())

    def test_moving_works_with_custom_dimensions(self):
        board = Board(rows=6, cols=5)
        robot = Robot()
        board.place(robot, x=2, y=4, f=Direction.NORTH)
        board.move(robot)
        self.assertEqual(Coordinates(2, 5, Direction.NORTH), board.report())


class TurningTestCase(unittest.TestCase):
    def test_can_turn_left_from_north(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.NORTH)
        robot.turn_left()
        board.move(robot)
        self.assertEqual(Coordinates(1, 2, Direction.WEST), board.report())

    def test_can_turn_left_from_east(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.EAST)
        robot.turn_left()
        board.move(robot)
        self.assertEqual(Coordinates(2, 3, Direction.NORTH), board.report())

    def test_can_turn_left_from_west(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.WEST)
        robot.turn_left()
        board.move(robot)
        self.assertEqual(Coordinates(2, 1, Direction.SOUTH), board.report())

    def test_can_turn_left_from_south(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.SOUTH)
        robot.turn_left()
        board.move(robot)
        self.assertEqual(Coordinates(3, 2, Direction.EAST), board.report())

    def test_can_turn_right_from_north(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.NORTH)
        robot.turn_right()
        board.move(robot)
        self.assertEqual(Coordinates(3, 2, Direction.EAST), board.report())

    def test_can_turn_right_from_east(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.EAST)
        robot.turn_right()
        board.move(robot)
        self.assertEqual(Coordinates(2, 1, Direction.SOUTH), board.report())

    def test_can_turn_right_from_west(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.WEST)
        robot.turn_right()
        board.move(robot)
        self.assertEqual(Coordinates(2, 3, Direction.NORTH), board.report())

    def test_can_turn_right_from_south(self):
        board = Board()
        robot = Robot()
        board.place(robot, x=2, y=2, f=Direction.SOUTH)
        robot.turn_right()
        board.move(robot)
        self.assertEqual(Coordinates(1, 2, Direction.WEST), board.report())


class OutOfBoundMovementsTestCase(unittest.TestCase):
    def setUp(self):
        self.moves: List[Tuple[Coordinates, OutOfBoundMovementException]] = [
            # First row
            (Coordinates(0, 0, Direction.SOUTH), SouthOutOfBoundException),
            (Coordinates(0, 0, Direction.WEST), WestOutOfBoundException),
            (Coordinates(1, 0, Direction.SOUTH), SouthOutOfBoundException),
            (Coordinates(2, 0, Direction.SOUTH), SouthOutOfBoundException),
            (Coordinates(3, 0, Direction.SOUTH), SouthOutOfBoundException),
            (Coordinates(4, 0, Direction.SOUTH), SouthOutOfBoundException),
            (Coordinates(4, 0, Direction.EAST), EastOutOfBoundException),
            # Second row
            (Coordinates(0, 1, Direction.WEST), WestOutOfBoundException),
            (Coordinates(4, 1, Direction.EAST), EastOutOfBoundException),
            # Third row
            (Coordinates(0, 2, Direction.WEST), WestOutOfBoundException),
            (Coordinates(4, 2, Direction.EAST), EastOutOfBoundException),
            # Fourth row
            (Coordinates(0, 3, Direction.WEST), WestOutOfBoundException),
            (Coordinates(4, 3, Direction.EAST), EastOutOfBoundException),
            # Fifth row
            (Coordinates(0, 4, Direction.NORTH), NorthOutOfBoundException),
            (Coordinates(0, 4, Direction.WEST), WestOutOfBoundException),
            (Coordinates(1, 4, Direction.NORTH), NorthOutOfBoundException),
            (Coordinates(2, 4, Direction.NORTH), NorthOutOfBoundException),
            (Coordinates(3, 4, Direction.NORTH), NorthOutOfBoundException),
            (Coordinates(4, 4, Direction.NORTH), NorthOutOfBoundException),
            (Coordinates(4, 4, Direction.EAST), EastOutOfBoundException),
        ]

    def test_moving_out_of_bounds_raises_an_exception(self):
        for coordinate, exception in self.moves:
            board = Board()
            robot = Robot()
            board.place(robot, x=coordinate.x, y=coordinate.y, f=coordinate.f)
            with self.assertRaises(exception):
                board.move(robot)
