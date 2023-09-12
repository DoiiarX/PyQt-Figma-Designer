from typing import Iterator


def indent(c: str | Iterator[str], n: int = 1) -> Iterator[str]:
    if isinstance(c, str):
        for line in c.splitlines():
            yield '    ' * n + line
        return

    for line in c:
        yield '    ' * n + line
