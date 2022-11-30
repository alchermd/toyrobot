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

## Implement a proper game loop