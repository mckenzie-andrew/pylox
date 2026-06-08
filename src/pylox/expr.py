from dataclasses import dataclass
from .tokens import Token

type Expr = Binary | Grouping | Literal | Unary


@dataclass
class Binary:
    left: Expr
    operator: Token
    right: Expr


@dataclass
class Grouping:
    expression: Expr


@dataclass
class Literal:
    value: object


@dataclass
class Unary:
    operator: Token
    right: Expr
