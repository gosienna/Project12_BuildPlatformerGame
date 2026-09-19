# Level 0: Quick Setup Check (about 5 minutes)

## Goal
Confirm the computer has Python 3.10+ and Arcade, and that a window can open. Nothing more. The learning about `.venv` and the terminal happens in [Level 1](level1_move_and_jump.md), once a game is running and every command gives a visible result.

## Concepts for the child
None to teach yet. The instructor says: *"Copy these commands exactly. In Level 1 we will find out what they do."*

> **One install only:** `arcade` is the only package this tutorial needs. See the dependency rule in [00_overview.md](00_overview.md).

## Build steps (instructor bites)

Progress: **run each check, and fix only what fails.**

- [ ] **0.1 Python.** Run `python3 --version` (Windows: `python --version`). Need **3.10 or newer**.
- [ ] **0.2 Arcade.** Run `python3 -c "import arcade; print(arcade.__version__)"`. Need **3.x**. If it fails and there is no `.venv` folder yet, use the fix below.
- [ ] **0.3 Hello window.** Create `check_setup.py` (below) and run it. A green window titled "Setup OK!" opens. Close it.

Any editor works (VS Code, Thonny, IDLE). Don't spend time choosing one.

### What to do with each result

| Result | Fix |
|---|---|
| Python missing or older than 3.10 | **Fix A** |
| `ModuleNotFoundError: No module named 'arcade'` | **Fix B** |
| Arcade version is 2.x | `pip install --upgrade "arcade>=3"` |
| Window doesn't open | **Fix C** |
| All three pass | Go to Level 1 |

### Fixes (show only the one that applies)

**Fix A: Install Python 3.10+**
- **macOS:** installer from python.org/downloads, or `brew install python`.
- **Windows:** installer from python.org/downloads. **Tick "Add python.exe to PATH"** on the first screen, then reopen the terminal.
- **Linux (Debian/Ubuntu):** `sudo apt install python3 python3-venv python3-pip`.

**Fix B: Make the project's toolbox and install Arcade** (copy exactly, one line at a time)
```
python3 -m venv .venv                 # Windows: python -m venv .venv
source .venv/bin/activate             # Windows: .venv\Scripts\activate
pip install arcade
```
The prompt now starts with `(.venv)`. If a later terminal stops working, run the second line again. Level 1 explains why.

**Fix C: Window problems**
- Update the graphics driver (Arcade needs OpenGL 3.3+).
- Apple Silicon Mac: use a native Python from python.org or Homebrew.
- Teacher on a machine with no screen: `xvfb-run -a python check_setup.py`.

## The check script

Save as `check_setup.py`.

```python
import arcade

window = arcade.Window(480, 200, "Setup OK!")
window.background_color = arcade.color.DARK_GREEN
arcade.run()
```

## How to test
- **Play test:** run `python3 check_setup.py` and a green window titled "Setup OK!" opens. Closing it ends the program with no error.
- **Automated (teacher):** `python3 -c "import sys, arcade; assert sys.version_info >= (3, 10) and int(arcade.__version__.split('.')[0]) >= 3"` exits with code 0.

## Done when
- [ ] Python 3.10+ is confirmed
- [ ] `import arcade` works (3.x)
- [ ] The green window opened and closed cleanly
