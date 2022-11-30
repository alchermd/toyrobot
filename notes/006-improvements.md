# Improvements

## Separate the parsing and sanitation logic to its own class

I've extracted the `_parse_command` and `_sanitize_input` into their own respective `Parser` and `Sanitizer` classes.
Default instances are also provided as to allow changing of parsers/sanitizers on runtime.

## Update sanitation of the PLACE command

Let's add a new entry on the test table:

```python
(
    [
        "PLACE       1,2,SOUTH     ",
        "MOVE   ",
        "  LEFT ",
        "   MOVE",
        "REPORT   ",
    ],
    ["Output: 2,1,EAST"],
),
```

The logic is now encapsulated nicely in the `Sanitizer` class due to the refactor in the previous step. Note that we
also added whitespace to the non-`PLACE` commands to make sure our updated sanitation works properly.

## Handle moving out of bounds

Let's add a new entry on the test table:

```python
(
    [
        "PLACE 4,3,SOUTH",
        "RIGHT",
        "RIGHT",
        "MOVE",
        "REPORT",
        "MOVE",
        "REPORT",
    ],
    ["Output: 4,4,NORTH", "Output: 4,4,NORTH"],
),
```

The test would fail because it will raise an `OutOfBoundMovementException` on the last `MOVE` command. The obvious fix
is to wrap the `.move` call inside a try-except block. For now, I just logged the error to stderr.

## Allow shorthand directions

We'll also start with new tests:

```python
(
    [
        "PLACE 2,2,N",
        "MOVE",
        "REPORT",
    ],
    ["Output: 2,3,NORTH"],
),
(
    [
        "PLACE 2,2,E",
        "MOVE",
        "REPORT",
    ],
    ["Output: 3,2,EAST"],
),
(
    [
        "PLACE 2,2,W",
        "MOVE",
        "REPORT",
    ],
    ["Output: 1,2,WEST"],
),
(
    [
        "PLACE 2,2,S",
        "MOVE",
        "REPORT",
    ],
    ["Output: 2,1,SOUTH"],
),
```

The solution is to augment the regex capture group into `(NORTH|EAST|WEST|SOUTH|N|E|W|S)`.

## Ignore invalid commands as well as those that occur before a PLACE command is issued

Starting with tests:

```python
(
    [
        "MOVE",
        "REPORT",
        "PLACE 2,2,S",
        "MOVE",
        "REPORT",
    ],
    ["Output: 2,1,SOUTH"],
),
(
    [
        "REPORT",
        "REPORT",
        "MOVE",
        "MOVE",
        "MOVE",
        "REPORT",
        "REPORT",
        "MOVE",
        "REPORT",
        "PLACE 2,2,N",
        "MOVE",
        "REPORT",
    ],
    ["Output: 2,3,NORTH"],
),
(
    [
        "FOO",
        "BAR",
        "PLACE 2,2,N",
        "MOVE",
        "REPORT",
    ],
    ["Output: 2,3,NORTH"],
),
```

To handle these scenarios, I created two new Exceptions: an `InvalidCommandException` and
an `UnparsableCommandException` that inherits from the former. These are then handled by the client class, in which the
errors are logged to stderr.

## Handle multiple PLACE commands

At this point, the code allows individual robots to be placed independent of each other. We can restrict this logic to
comply with the spec. First, the test:

```python
(
    [
        "PLACE 1,4,W",
        "PLACE 0,0,W",
        "PLACE 2,2,N",
        "MOVE",
        "REPORT",
        "PLACE 0,0,W",
        "REPORT",
    ],
    ["Output: 2,3,NORTH", "Output: 0,0,WEST"],
),
```

The solution that I chose is to implement a `reset` method on the `Board` class that does what its name implies: reset
the board state back to empty. I then call this reset method before placing a robot.

## Implement a proper game loop