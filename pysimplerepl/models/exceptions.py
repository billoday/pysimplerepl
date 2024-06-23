from typing import Optional


class InvalidFlag(ValueError):
    def __init__(self, message: Optional[str] = None, *args: object) -> None:
        if message is None:
            message = 'invalid flag'
        super().__init__(message, *args)


class InsufficientArgsError(Exception):
    pass



class CommandNotFoundError(Exception):
    pass