from dataclasses import dataclass
from .expr import Expr
from typing import Union


@dataclass(frozen=True)
class Expression:
    expression: Expr


@dataclass(frozen=True)
class Print:
    expression: Expr


Stmt = Union[Expression, Print]