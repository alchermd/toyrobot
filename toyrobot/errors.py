class OutOfBoundMovementException(Exception):
    pass


class NorthOutOfBoundException(OutOfBoundMovementException):
    pass


class EastOutOfBoundException(OutOfBoundMovementException):
    pass


class WestOutOfBoundException(OutOfBoundMovementException):
    pass


class SouthOutOfBoundException(OutOfBoundMovementException):
    pass
