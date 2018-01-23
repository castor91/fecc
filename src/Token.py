from enum import Enum

class Token(Enum):
    @classmethod
    def has(cls, value):
        return any(value == item.value for item in cls)

    @classmethod
    def get(cls, token):
        return [name for name, member in cls.__members__.items() if member.value == token][0]