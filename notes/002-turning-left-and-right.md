# Turning Left and Right

Writing tests for turning left is straightforward:

```python
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
```

The logic is simple enough -- change the robot's current direction to it's left. It's also worth noting that the robot's
direction is stored in the robot itself, not on the board state. I made this decision solely by the fact that physically
turning the robot won't have anything to do with the board.

Turning right is essentially the same:

```python
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
```

## Notes

The test cases are starting to look repetitive. But at this early stage, I'm not too eager refactoring repeated code. I
believe it's best to let the codebase grow organically and let the "ickyness" bubble up. Only then I'll consider
refactoring, as I find that premature optimization has always been more costly than a few copy-paste here and there.

But to keep things tidy, I decided to separate the testcases to their own distinct classes as they test different
behaviors (basic movement and turning).