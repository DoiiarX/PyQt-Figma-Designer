from typing import Iterator


def indent(c: str | Iterator[str], n: int = 1) -> Iterator[str]:
    if isinstance(c, str):
        print('indenting', c)
        for line in c.splitlines():
            yield '    ' * n + line
        print('returning')
        return

    for line in c:
        print('iter-indenting', line)
        yield '    ' * n + line
