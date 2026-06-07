import sys
from pathlib import Path
from .scanner import Scanner

had_error = False


def report(line: int, where: str, message: str) -> None:
    global had_error
    print(f"[line {line}] Error {where}: {message}", file=sys.stderr)
    had_error = True


def error(line: int, message: str) -> None:
    report(line, "", message)


def run(source: str) -> None:
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)


def run_file(path: Path) -> None:
    global had_error
    text = path.read_text()
    run(text)

    if had_error:
        sys.exit(65)


def run_prompt() -> None:
    global had_error
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        run(line)
        had_error = False


def main(args: list[str]) -> None:
    args_length = len(args)

    if args_length > 1:
        print("Usage: jlox [script]", file=sys.stderr)
        sys.exit(64)
    elif args_length == 1:
        file = Path(args[0])
        run_file(file)
    else:
        run_prompt()


if __name__ == "__main__":
    main(sys.argv[1:])
