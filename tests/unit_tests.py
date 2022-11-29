import unittest

from toyrobot.models import Board, Robot, Direction, Coordinates


class BoardTestCase(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
