# Initial Setup

The documents within this directory are personal notes of my thought process as I try to accomplish the given
specifications
for the Toy Robot Code Challenge. There's no particular format that I follow, so treat these documents as a "braindump".

## First tests, and modelling the domain problem

To start, I extracted the key requirements and constraints from the instruction document:

1. A toy robot is placed on a 5x5 board
2. The robot can roam around the table, but not fall out of it.
3. The board can be interfaced with via the following commands:
    1. `PLACE X, Y, F` - places the robot in the `(x, y)` coordinates facing the `F` direction
    2. `MOVE` - moves the robot one square towards the direction it's currently facing.
    3. `LEFT` - rotate the robot to its left from the direction it's currently facing
    4. `RIGHT` - rotate the robot to its right from the direction it's currently facing
    5. `REPORT` - display's the current robot's location in the format of `x, y, f`
4. Invalid commands, as well as those with invalid syntax, will be ignored.

With this information, I decided that a good starting point is to write tests for the minimum valid actions: placing the
robot and reporting its location. I'm focusing on the internal API here: at this point I don't necessarily care that the
final application will be interacting to stdin/stdout for its input/output.

```python
 def test_can_place_the_robot_in_the_board_and_report_its_location(self):
     board = Board()
     robot = Robot()
     board.place(robot, x=2, y=2, f=Direction.NORTH)
     self.assertEqual(Coordinates(2, 2, Direction.NORTH), board.report())
```

I've decided to make the `Board` class "manage" the `Robot` and all the movement related logic. This allows the `Board`
class to be extensible in the future to allow other potential entities to be placed inside it without being tied to how
a `Robot` behaves. I decided to make an enum of directions and a dataclass to represent the coordinates as I prefer to
work with type hints (I really think they make for "self-documenting" code).

Next up is testing for directional movements

```python
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
```

After an hour of drawing up the board on physical paper, as well as considering how coordinates to index translation
would happen (i.e mapping `(x, y)` to index `z`), I've decided to use a list of length `nrows * ncols` as the in-memory
storage of the board. I've used a 2D list on similar board games before, so I knew how easy it is to get lost in the
translation logic as the mental model for the physical board and the in-memory board doesn't really match up
(ex: `(0, 0)` (bottom left) isn't really directly stored in `list[0][0]` (top left)).

Although not in the spec, I've decided to make the `Board`'s dimension dynamic. This seems to be a feature that could
realistically be implemented in the future and its implementation isn't really too hard.

```python
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
```