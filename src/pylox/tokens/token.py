from .token_type import TokenType
from dataclasses import dataclass


@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: object
    line: int
