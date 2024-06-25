import abc
from typing import List


class Sanitizer:
    """
    Base Sanitizer class, intended to host the logic for cleaning up raw user input.
    """

    @abc.abstractmethod
    def sanitize_raw_input(self, raw_input: str) -> List[str]:
        """
        Sanitizes the given raw input string.
        """
        raise NotImplementedError


class CommandSanitizer(Sanitizer):
    """
    Basic Sanitizer implementation.
    """

    def sanitize_raw_input(self, raw_input: str) -> List[str]:
        """
        Removes whitespaces, including those in-between strings. Example:
        in: "PLACE       1,2,SOUTH     \n  MOVE   \nLEFT\nMOVE\n  REPORT\n"
        out: ["PLACE 1,2,SOUTH", "MOVE", "LEFT", "MOVE", "REPORT]
        """
        return [
            " ".join(list(filter(lambda x: x, command.strip().upper().split(" "))))
            for command in raw_input.split("\n")
        ]
