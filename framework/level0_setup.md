# Level 0: Setup Check

## Goal
Before any game code, confirm the computer can run Python and Arcade. If something is missing, give the child (or parent) the exact instructions to fix it. Level 1 starts only when the check passes.

## Concepts for the child
What Python is, what a terminal is (typing commands instead of clicking), what a library is (`arcade`), and what a virtual environment is: **a private toolbox for one project**. The `.venv` folder holds its own copy of Python and its own libraries, so this project can't break other projects (and they can't break it).

## Key components

| Component | Responsibility | Tool |
|---|---|---|
| Python interpreter | Runs the `.py` files | `python3` (macOS/Linux) or `python` / `py` (Windows), version 3.10+ |
| Virtual environment | Keeps this project's libraries separate | `python3 -m venv .venv` |
| Arcade library | The game toolkit used in every level | `pip install arcade` (3.x) |
| Editor | Where the child types code | VS Code, Thonny or IDLE |
| Check script | Proves a window can open | `check_setup.py` (below) |
| Detective script | Proves *which* Python runs your code | `where_am_i.py` (below) |

> **One install only:** `arcade` is the only package this tutorial needs. Don't install numpy, matplotlib, pygame or anything else. See the dependency rule in [00_overview.md](00_overview.md).

## Build steps (instructor bites)

Progress: **run the check first**, then fix only what fails.

- [ ] **0.1 Check Python.** Run `python3 --version` (Windows: `python --version` or `py --version`). Need **3.10 or newer**.
- [ ] **0.2 Check the environment.** Look for a `.venv` folder in the project. Check whether it is active (the terminal prompt shows `(.venv)`).
- [ ] **0.3 Check Arcade.** Run `python3 -c "import arcade; print(arcade.__version__)"`. Need **3.x**.
- [ ] **0.4 Check a window opens.** Run `python3 check_setup.py` and look for a window with the text "Setup OK".
- [ ] **0.5 If anything failed,** show only the matching fix from "Fix instructions" below, then re-run the failed check.
- [ ] **0.6 Pick an editor** (if the child has none) and confirm they can run a file from it or from the terminal.
- [ ] **0.7 Explore the `.venv`** with the command-line mini-goals below. The child does each one, reads the output aloud, and says what it proves.

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

## Mini-goals: meet your `.venv` on the command line

Purpose: the child sees with their own eyes that **the Python inside `.venv`** runs their scripts, and gets comfortable in the terminal. Windows equivalents are in brackets. Do them in order; each takes about a minute.

| # | Goal | Command | What to notice |
|---|---|---|---|
| 1 | Know where you are | `pwd` [`cd`] then `ls` [`dir`] | The terminal is always "standing" in one folder. You should see `.venv` and your `.py` files. |
| 2 | Look inside the toolbox | `ls .venv` then `ls .venv/bin` [`dir .venv\Scripts`] | `.venv` is just a normal folder. Inside `bin` [`Scripts`] you will find `python`, `pip` and `activate`. **That `python` is the one we want to use.** |
| 3 | Ask "which Python?" (activated) | `source .venv/bin/activate` [`.venv\Scripts\activate`] then `which python` [`where python`] | The path ends in `.venv/bin/python`. The prompt also shows `(.venv)`. |
| 4 | Run the detective script | `python where_am_i.py` | It prints `Inside a .venv? YES`, and the arcade path is inside `.venv`. |
| 5 | Turn the toolbox off | `deactivate` then `which python3` [`where python`] then `python3 where_am_i.py` | The path is now the system Python. It says `Inside a .venv? NO`, and usually `arcade` is **NOT INSTALLED** here. This shows arcade lives only in the `.venv`. |
| 6 | Use it without activating | `.venv/bin/python where_am_i.py` [`.venv\Scripts\python where_am_i.py`] | It says YES again, even though `(.venv)` is not showing. "Activate" only changes which `python` the terminal finds first. |
| 7 | Compare the libraries | Activated: `pip list`. Deactivated: `python3 -m pip list` | Two different lists. The `.venv` list is short and has `arcade`. Two toolboxes, two contents. |

After goal 7, ask the child: **"Why don't we just install arcade for the whole computer?"** A good answer: different projects can need different versions, and mistakes stay inside one folder that can be deleted and rebuilt.

**Bonus:** delete `.venv` (`rm -rf .venv` [`rmdir /s /q .venv`]), then rebuild it with the three Fix B commands. The child learns that `.venv` is disposable and the project files are safe.

### The detective script

Save as `where_am_i.py`.

```python
import sys

in_venv = sys.prefix != sys.base_prefix

print("Python running this script:", sys.executable)
print("Inside a .venv?           :", "YES" if in_venv else "NO")
print("Its home folder           :", sys.prefix)

try:
    import arcade
    print("arcade found at           :", arcade.__file__)
except ModuleNotFoundError:
    print("arcade found at           : NOT INSTALLED for this Python")
```

Expected when the `.venv` Python runs it (paths will differ):
```
Python running this script: /Users/sam/platformer/.venv/bin/python
Inside a .venv?           : YES
Its home folder           : /Users/sam/platformer/.venv
arcade found at           : /Users/sam/platformer/.venv/lib/python3.12/site-packages/arcade/__init__.py
```

Two ways to read it: the first line shows **the exact Python** that ran the script, and `YES` is the proof it lives in `.venv`.

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
- **Runs inside the venv:** `.venv/bin/python -c "import sys; assert sys.prefix != sys.base_prefix"` exits with code 0. The same command with the system `python3` must fail. That is the proof the `.venv` is really isolated.
- **Headless smoke test:** `xvfb-run -a python -c "import arcade; w = arcade.Window(100, 100); w.close()"` exits with code 0 (Linux/CI only).

## Done when
- [ ] Python 3.10+ is confirmed
- [ ] `.venv` exists and the child knows how to activate it
- [ ] The child completed the mini-goals and can explain in one sentence what `.venv` is for
- [ ] `where_am_i.py` said `Inside a .venv? YES` when activated and `NO` after `deactivate`
- [ ] The child can use `pwd`, `ls`, `cd`, `activate` and `deactivate` without help
- [ ] `import arcade` works and the version is 3.x
- [ ] `pip list` shows nothing extra was installed by hand
- [ ] The "Setup OK!" window opened and closed cleanly
- [ ] The child has an editor and can run a file
