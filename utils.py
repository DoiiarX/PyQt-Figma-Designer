from typing import Iterator


def indent(c: str | Iterator[str], n: int = 1) -> str | Iterator[str]:
    if isinstance(c, str):
        for line in c.splitlines():
            yield '    ' * n + line
    for line in c:
        yield '    ' * n + line
