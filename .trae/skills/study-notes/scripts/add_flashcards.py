"""把记忆卡片 JSON 追加登记到间隔重复复习表 flashcards.csv。

用法: python add_flashcards.py <cards.json> <flashcards.csv>
cards.json 为数组，每项含 subject / topic / question / answer 四个字段。
"""
import csv
import json
import sys
from datetime import date, timedelta
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 3:
        print("用法: python add_flashcards.py <cards.json> <flashcards.csv>")
        sys.exit(1)

    cards = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not isinstance(cards, list) or not cards:
        print("cards.json 必须是非空数组")
        sys.exit(1)
    required = {"subject", "topic", "question", "answer"}
    for i, c in enumerate(cards):
        missing = required - set(c)
        if missing:
            print(f"第 {i + 1} 张卡片缺少字段: {', '.join(sorted(missing))}")
            sys.exit(1)

    csv_path = Path(sys.argv[2])
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not csv_path.exists()
    today = date.today()
    next_review = today + timedelta(days=1)

    # utf-8-sig 便于用 Excel 直接打开不乱码
    with csv_path.open("a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["科目", "主题", "问题", "答案", "创建日期", "下次复习"])
        for c in cards:
            writer.writerow([
                c["subject"], c["topic"], c["question"], c["answer"],
                today.isoformat(), next_review.isoformat(),
            ])

    print(f"已登记 {len(cards)} 张卡片 -> {csv_path}（下次复习: {next_review}）")


if __name__ == "__main__":
    main()
