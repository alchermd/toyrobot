# Implementing the client

At this point I'm pretty satisfied with the API, and it's time to implement the "frontend client" that the end user will
interact with. Admittedly, I haven't tried testing CLI apps in Python before, so I'm just applying the concepts that I
knew with Golang -- monkey patching stdin/stdout and capturing the streams on a list that the testcase can track. As
with the previous testcase, I'll use table-based tests:

```python
class ConsoleClientTestCase(unittest.TestCase):
    def setUp(self):
        self.commands: List[Tuple[List[str], List[str]]] = [
            (
                [
                    "PLACE 0,0,NORTH",
                    "MOVE",
                    "REPORT",
                ],
                ["Output: 0,1,NORTH"],
            ),
            (
                [
                    "PLACE 0,0,NORTH",
                    "LEFT",
                    "REPORT",
                ],
                ["Output: 0,0,WEST"],
            ),
            (
                [
                    "PLACE 1,2,EAST",
                    "MOVE",
                    "MOVE",
                    "LEFT",
                    "MOVE",
                    "REPORT",
                ],
                ["Output: 3,3,NORTH"],
            ),
        ]

    def test_can_process_commands_with_expected_results(self):
        for commands, expected_output in self.commands:
            received_output = []
            toyrobot.client.input = lambda _: "\n".join(commands)
            toyrobot.client.print = lambda s: received_output.append(s)
            client = toyrobot.client.ConsoleClient()
            client.start()
            self.assertEqual(expected_output, received_output)
```

At this point I've managed to make the tests pass using a capture-sanitize-execute flow. There's still a lot of room for
improvement:

- Sanitation and parsing logic is stored in the client class. Ideally, a separate class should handle this to allow
  extensibility in the future
- The parsing logic only takes into account the input from the testcase: an input like `PLACE       0,0,NORTH` would
  still be deemed invalid
- Moving out of bounds will fail the tests
- UX could be improved by allowing shorthand directions such as "N" for "North" etc.
- There's no "game loop" yet -- the client is only consuming a single string (separated by `\n`) instead of a stream