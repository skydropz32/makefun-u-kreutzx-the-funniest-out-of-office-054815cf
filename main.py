"""The Funniest Out-of-Office: writes one out-of-office line to /output/entry.txt."""

from pathlib import Path

LINE = "Out of office until Monday. My laptop is on; I am not. We have agreed to this arrangement."


def main() -> None:
    # Gate: the entry must be 1-140 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line must be 1-140 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
