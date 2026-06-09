from .expr import Expr, Binary, Unary, Grouping, Literal
from .tokens import Token, TokenType
from .errors import LoxRuntimeError
from typing import assert_never


def interpret(expr: Expr) -> object:
    return evaluate(expr)


def is_truthy(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return True


def is_equal(a: object, b: object) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if isinstance(a, bool) != isinstance(b, bool):
        return False
    return a == b


def check_number_operand(op: Token, operand: object) -> None:
    if isinstance(operand, float):
        return
    raise LoxRuntimeError(op, "Operand must be a number.")


def check_number_operands(op: Token, left: object, right: object) -> None:
    if isinstance(left, float) and isinstance(right, float):
        return
    raise LoxRuntimeError(op, "Operands must be numbers.")


def evaluate_binary(op: Token, left: object, right: object) -> object:
    match op.type:
        case TokenType.GREATER:
            check_number_operands(op, left, right)
            assert isinstance(left, float) and isinstance(right, float)
            return left > right
        case TokenType.GREATER_EQUAL:
            check_number_operands(op, left, right)
            assert isinstance(left, float) and isinstance(right, float)
            return left >= right
        case TokenType.LESS:
            check_number_operands(op, left, right)
            assert isinstance(left, float) and isinstance(right, float)
            return left < right
        case TokenType.LESS_EQUAL:
            check_number_operands(op, left, right)
            assert isinstance(left, float) and isinstance(right, float)
            return left <= right
        case TokenType.MINUS:
            check_number_operands(op, left, right)
            assert isinstance(left, float) and isinstance(right, float)
            return left - right
        case TokenType.SLASH:
            check_number_operands(op, left, right)
            assert isinstance(left, float) and isinstance(right, float)
            return left / right
        case TokenType.STAR:
            check_number_operands(op, left, right)
            assert isinstance(left, float) and isinstance(right, float)
            return left * right
        case TokenType.PLUS:
            if isinstance(left, float) and isinstance(right, float):
                return left + right
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            raise LoxRuntimeError(op, "Operands must be two numbers or two strings.")
        case TokenType.BANG_EQUAL:
            return not is_equal(left, right)
        case TokenType.EQUAL_EQUAL:
            return is_equal(left, right)
        case _:
            raise LoxRuntimeError(op, f"Unsupported binary operator '{op.lexeme}'.")


def evaluate(expr: Expr) -> object:
    match expr:
        case Literal(value=v):
            return v
        case Grouping(expression=inner):
            return evaluate(inner)
        case Unary(operator=op, right=r):
            right = evaluate(r)
            match op.type:
                case TokenType.MINUS:
                    check_number_operand(op, right)
                    assert isinstance(right, float)
                    return -right
                case TokenType.BANG:
                    return not is_truthy(right)
                case _:
                    raise LoxRuntimeError(op, f"Unsupported unary operator '{op.lexeme}'.")
        case Binary(left=l, operator=op, right=r):
            left = evaluate(l)
            right = evaluate(r)
            return evaluate_binary(op, left, right)
        case _:
            assert_never(expr)