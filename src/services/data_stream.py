from pathlib import Path
from typing import Iterator

from src.utils.decorators import timer
from src.utils.logger import get_logger

log = get_logger(__name__, "logs/app.log")


def read_lines(path: str) -> Iterator[str]:
    """逐行读，惰性生成器."""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


def filter_errors(lines: Iterator[str]) -> Iterator[str]:
    """只保留含 ERROR 的行."""
    for line in lines:
        if "ERROR" in line:
            yield line


def add_prefix(lines: Iterator[str], tag: str) -> Iterator[str]:
    """给每行加前缀."""
    for line in lines:
        yield f"[{tag}] {line}"


@timer()
def pipeline(src: str, dst: str) -> int:
    """读 → 过滤 → 加前缀 → 写，全程流式."""
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    count = 0
    pipe = add_prefix(filter_errors(read_lines(src)), "ERR")
    with open(dst, "w", encoding="utf-8") as out:
        for line in pipe:
            out.write(line + "\n")
            count += 1
    log.info("处理完成: 写入 %d 行 → %s", count, dst)
    return count


if __name__ == "__main__":
    pipeline("data/raw/user.txt", "data/processed/errors.log")
