# UX Improvement

While I was playing around the `Board` and `Robot`'s API, I found a sneaky "bug" in the current code:

```python
board = Board()
robot = Robot()
board.place(robot, 2, 2, "NORTH")
robot.turn_right()
board.report() # Shows 2, 2, "NORTH" while we expect it to show 2, 2, "EAST"
```

After a few minutes of debugging, I found out a small quirk in my implementation: since I used an enum to represent the
directions, directly using a string such as "NORTH" will fail any of the `match-case` statements that I had in my code.


```python
direction = "NORTH"
match direction:
    case Direction.NORTH:
        # Code will not enter this branch as "NORTH" == Direction.NORTH evaluates to False!
```

In order to make the comparison work, my `Direction` class needs to inherit from the base `str` class. Digging deeper, 
I found that `Enum` can be used as a mixin. Since I've decided that it's bad UX to force the user to import the enum 
value instead of passing a string. So the solution to this "bug" is to change the class definition to 
`class Direction(str, Enum)`.

Lastly, I decided to install `ipython` to improve my debugging experience while.