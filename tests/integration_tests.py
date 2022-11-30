import unittest
from typing import List, Tuple

import toyrobot.client


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
