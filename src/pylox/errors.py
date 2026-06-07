import sys

had_error = False


def report(line: int, where: str, message: str) -> None:
    global had_error
    print(f"[line {line}] Error {where}: {message}", file=sys.stderr)
    had_error = True


def error(line: int, message: str) -> None:
    report(line, "", message)


def reset() -> None:
    global had_error
    had_error = False
