from typing import List


class Sanitizer:
    def sanitize_raw_input(self, raw_input: str) -> List[str]:
        raise NotImplementedError


class CommandSanitizer(Sanitizer):
    def sanitize_raw_input(self, raw_input: str) -> List[str]:
        return [command.strip().upper() for command in raw_input.split("\n")]
