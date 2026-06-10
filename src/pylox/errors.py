import sys
from .tokens import Token, TokenType

had_error = False
had_runtime_error = False


class ParseError(Exception):
    pass


class LoxRuntimeError(RuntimeError):
    def __init__(self, token: Token, message: str) -> None:
        super().__init__(message)
        self.token = token


def report(line: int, where: str, message: str) -> None:
    global had_error
    print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
    had_error = True


def error(line: int, message: str) -> None:
    report(line, "", message)


def runtime_error(error: LoxRuntimeError) -> None:
    global had_runtime_error
    print(f"{error}\n[line {error.token.line}]", file=sys.stderr)
    had_runtime_error = True


def error_token(token: Token, message: str) -> None:
    if token.type == TokenType.EOF:
        report(token.line, " at end", message)
    else:
        report(token.line, f" at '{token.lexeme}'", message)


def reset() -> None:
    global had_error, had_runtime_error
    had_error = False
    had_runtime_error = True
