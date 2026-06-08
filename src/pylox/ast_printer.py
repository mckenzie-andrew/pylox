from .expr import Expr, Binary, Grouping, Literal, Unary
from typing import assert_never


def print_ast(expr: Expr) -> str:
    match expr:
        case Binary(left=l, operator=op, right=r):
            return f"({op.lexeme} {print_ast(l)} {print_ast(r)})"
        case Grouping(expression=inner):
            return f"(group {print_ast(inner)})"
        case Literal(value=v):
            return "nil" if v is None else str(v)
        case Unary(operator=op, right=r):
            return f"({op.lexeme} {print_ast(r)})"
        case _:
            assert_never(expr)