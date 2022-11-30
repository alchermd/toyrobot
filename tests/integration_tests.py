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
        ]

    def test_can_process_commands_with_expected_results(self):
        for commands, expected_output in self.commands:
            received_output = []
            toyrobot.client.input = lambda _: "\n".join(commands)
            toyrobot.client.print = lambda s: received_output.append(s)
            client = toyrobot.client.ConsoleClient()
            client.start()
            self.assertEqual(expected_output, received_output)
