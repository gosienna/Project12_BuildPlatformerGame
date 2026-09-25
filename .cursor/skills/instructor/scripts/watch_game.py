"""Restart the game starter when any .py file under game/ is saved.

Run from the repo root:

    .venv/bin/python .cursor/skills/instructor/scripts/watch_game.py
    .venv/bin/python .cursor/skills/instructor/scripts/watch_game.py game/level2.py
"""

import subprocess
import sys
import time
from pathlib import Path

POLL_SECONDS = 0.4
GAME_DIR = Path("game")
DEFAULT_STARTER = GAME_DIR / "level1.py"


def sources():
    files = []
    for path in GAME_DIR.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        files.append(path)
    return files


def snapshot():
    return {path: path.stat().st_mtime for path in sources()}


def changed_paths(before, after):
    changed = []
    for path in sorted(set(before) | set(after), key=str):
        if path not in before:
            changed.append(f"new {path}")
        elif path not in after:
            changed.append(f"deleted {path}")
        elif before[path] != after[path]:
            changed.append(str(path))
    return changed


def stop(proc):
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()


def main():
    starter = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_STARTER
    if not GAME_DIR.is_dir():
        print(
            f"Missing folder: {GAME_DIR.resolve()} "
            "(create it and put the game scripts there)",
            file=sys.stderr,
        )
        sys.exit(1)
    if not starter.is_file():
        print(f"Missing starter script: {starter}", file=sys.stderr)
        sys.exit(1)

    print(f"Watching {GAME_DIR}/ for .py saves. Starter: {starter}")
    print("Stop with Ctrl+C.")
    seen = snapshot()
    proc = subprocess.Popen([sys.executable, str(starter)])
    try:
        while True:
            time.sleep(POLL_SECONDS)
            fresh = snapshot()
            delta = changed_paths(seen, fresh)
            if not delta:
                continue
            seen = fresh
            print("Restart:", ", ".join(delta))
            stop(proc)
            proc = subprocess.Popen([sys.executable, str(starter)])
    finally:
        stop(proc)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped watcher.")
