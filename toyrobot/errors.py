class OutOfBoundMovementException(Exception):
    """
    Generic exception for movements that would make the robot fall out of bounds.
    """


class NorthOutOfBoundException(OutOfBoundMovementException):
    pass


class EastOutOfBoundException(OutOfBoundMovementException):
    pass


class WestOutOfBoundException(OutOfBoundMovementException):
    pass


class SouthOutOfBoundException(OutOfBoundMovementException):
    pass


class InvalidCommandException(Exception):
    """
    Generic exception for commands that are not supported by the parser.
    """


class UnparsableCommandException(InvalidCommandException):
    """
    Exception for commands that failed the parser's pattern matching.
    """


class InvalidPlacementException(Exception):
    """
    Exception for invalid placement of the robot on the board, such as incorrect coordinate addressing.
    """
