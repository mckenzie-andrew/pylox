import sys
from pathlib import Path
from .scanner import Scanner
from . import errors


def run(source: str) -> None:
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)


def run_file(path: Path) -> None:
    text = path.read_text()
    run(text)

    if errors.had_error:
        sys.exit(65)


def run_prompt() -> None:
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        run(line)
        errors.reset()


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
