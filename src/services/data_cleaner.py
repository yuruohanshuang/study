from src.utils.logger import get_logger

log = get_logger(__name__, "logs/app.log")


def clean_lines(path: str) -> list[str]:
    """读文件，去空行、去前后空格、去重，保持原顺序."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.readlines()
    except FileNotFoundError:
        log.error("文件不存在: %s", path)
        return []

    seen, result = set(), []
    for line in raw:
        s = line.strip()
        if not s or s in seen:
            continue
        seen.add(s)
        result.append(s)

    log.info("原始 %d 行 → 清洗后 %d 行", len(raw), len(result))
    return result


def group_by_city(rows: list[tuple[str, str]]) -> dict[str, int]:
    """按城市分组统计."""
    stats = {}
    for _, city in rows:
        stats[city] = stats.get(city, 0) + 1
    return stats


if __name__ == "__main__":
    lines = clean_lines("data/raw/users.txt")
    log.info("去重后样例: %s", lines[:3])

    students = [("张三", "北京"), ("李四", "上海"), ("王五", "北京")]
    log.info("城市分组: %s", group_by_city(students))
