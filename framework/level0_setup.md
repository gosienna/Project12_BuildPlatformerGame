# Level 0: Setup Check

## Goal
Before any game code, confirm the computer can run Python and Arcade. If something is missing, give the child (or parent) the exact instructions to fix it. Level 1 starts only when the check passes.

## Concepts for the child
What Python is, what a terminal is, what a library is (`arcade`), and what a virtual environment is (a private toolbox for one project).

## Key components

| Component | Responsibility | Tool |
|---|---|---|
| Python interpreter | Runs the `.py` files | `python3` (macOS/Linux) or `python` / `py` (Windows), version 3.10+ |
| Virtual environment | Keeps this project's libraries separate | `python3 -m venv .venv` |
| Arcade library | The game toolkit used in every level | `pip install arcade` (3.x) |
| Editor | Where the child types code | VS Code, Thonny or IDLE |
| Check script | Proves a window can open | `check_setup.py` (below) |

## Build steps (instructor bites)

Progress: **run the check first**, then fix only what fails.

- [ ] **0.1 Check Python.** Run `python3 --version` (Windows: `python --version` or `py --version`). Need **3.10 or newer**.
- [ ] **0.2 Check the environment.** Look for a `.venv` folder in the project. Check whether it is active (the terminal prompt shows `(.venv)`).
- [ ] **0.3 Check Arcade.** Run `python3 -c "import arcade; print(arcade.__version__)"`. Need **3.x**.
- [ ] **0.4 Check a window opens.** Run `python3 check_setup.py` and look for a window with the text "Setup OK".
- [ ] **0.5 If anything failed,** show only the matching fix from "Fix instructions" below, then re-run the failed check.
- [ ] **0.6 Pick an editor** (if the child has none) and confirm they can run a file from it or from the terminal.

### Decision table (what the instructor does with each result)

| Check result | Meaning | Action |
|---|---|---|
| `command not found` / "Python was not found" | Python missing | Fix A |
| Version below 3.10 | Python too old | Fix A |
| `ModuleNotFoundError: No module named 'arcade'` | Arcade missing | Fix B (make venv first if none) |
| Arcade version is 2.x | Wrong version | Fix C |
| Window does not open, or crashes | Graphics or display problem | Fix D |
| All pass | Ready | Go to Level 1 |

### Fix instructions (show only the one that applies)

**Fix A: Install Python 3.10+**
- **macOS:** download the installer from python.org/downloads, or run `brew install python`.
- **Windows:** download from python.org/downloads. On the first installer screen, **tick "Add python.exe to PATH"**, then click Install. Close and reopen the terminal afterwards.
- **Linux (Debian/Ubuntu):** `sudo apt install python3 python3-venv python3-pip`.
- Then re-run check 0.1.

**Fix B: Create a virtual environment and install Arcade**
```
cd <project folder>
python3 -m venv .venv                 # Windows: python -m venv .venv
source .venv/bin/activate             # Windows: .venv\Scripts\activate
pip install arcade
```
- The prompt should now start with `(.venv)`.
- Every new terminal needs the `activate` line again. This is the most common "it stopped working" cause.
- Then re-run checks 0.3 and 0.4.

**Fix C: Wrong Arcade version**
```
pip install --upgrade "arcade>=3"
```

**Fix D: Window problems**
- Update the graphics driver (Windows/Linux). Arcade needs OpenGL 3.3 or newer.
- Remote or headless machine: run with `xvfb-run -a python check_setup.py`. This is for teachers only. A child needs a real screen.
- On Apple Silicon Macs, make sure Python is a native arm64 build (from python.org or Homebrew), not an old x86 one.

## The check script

Save as `check_setup.py`. It also reports Python and Arcade versions, so the instructor can read the result at a glance.

```python
import sys
import arcade

print("Python :", sys.version.split()[0])
print("Arcade :", arcade.__version__)

class SetupWindow(arcade.Window):
    def __init__(self):
        super().__init__(480, 200, "Setup check")
        self.text = arcade.Text("Setup OK! Close this window.", 40, 90, arcade.color.WHITE, 18)
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        self.clear()
        self.text.draw()

SetupWindow()
arcade.run()
```

## How to test

### Play test checklist
| Action | Expected |
|---|---|
| Run `python3 check_setup.py` | A green window opens showing "Setup OK!" |
| Read the terminal | Python is 3.10 or newer, Arcade is 3.x |
| Close the window | The program ends with no error |
| Open a **new** terminal, activate `.venv`, run again | Still works (proves the child can repeat it) |

### Automated checks (for the adult or teacher)
- **Python version:** `python3 -c "import sys; assert sys.version_info >= (3, 10)"` exits with code 0.
- **Arcade version:** `python3 -c "import arcade; assert int(arcade.__version__.split('.')[0]) >= 3"` exits with code 0.
- **Headless smoke test:** `xvfb-run -a python -c "import arcade; w = arcade.Window(100, 100); w.close()"` exits with code 0 (Linux/CI only).

## Done when
- [ ] Python 3.10+ is confirmed
- [ ] `.venv` exists and the child knows how to activate it
- [ ] `import arcade` works and the version is 3.x
- [ ] The "Setup OK!" window opened and closed cleanly
- [ ] The child has an editor and can run a file
