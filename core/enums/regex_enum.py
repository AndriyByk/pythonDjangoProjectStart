from enum import Enum


class RegEx(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,20}$',
        'First letter should be A-Z, others - letters or digits, min length - 2 symbols, max length - 20 symbols'
    )

    AUTO_PARK_NAME = (
        r'^[A-Z][a-zA-Z]{1,20}$',
        'First letter should be A-Z, digits are restricted min length 2 symbols, max length 20 symbols'
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg