# Level 0: Setup Check — progress

Learner: kw
Branch: kw
Source plan: `framework/level0_setup.md`

Progress: **bite 6 of 15** — waiting for mini-goal 1 (`pwd` / `ls`)

## Bites

### Setup checks (0.1–0.4)

- [x] **1.** Check Python 3.10+ (`python3 --version`)
- [x] **2.** Check `.venv` exists and is activated (prompt shows `(.venv)`)
- [x] **3.** Check Arcade 3.x (`import arcade; print(arcade.__version__)`) — install only `arcade` if missing
- [x] **4.** Check a window opens: create `check_setup.py`, run it, see green "Setup OK!"
- [x] **5.** Create `where_am_i.py` (detective script)

### Mini-goals: meet your `.venv` (0.7)

- [ ] **6.** Know where you are — `pwd` then `ls` (see `.venv` and your `.py` files)
- [ ] **7.** Look inside the toolbox — `ls .venv` then `ls .venv/bin` (find `python`, `pip`, `activate`)
- [ ] **8.** Ask "which Python?" (activated) — `which python` path ends in `.venv/bin/python`
- [x] **9.** Run the detective script (activated) — `python where_am_i.py` prints `YES` and arcade inside `.venv`
- [ ] **10.** Turn the toolbox off — `deactivate`, then `which python3`, then `python3 where_am_i.py` → `NO` / arcade usually NOT INSTALLED
- [ ] **11.** Use it without activating — `.venv/bin/python where_am_i.py` → `YES` even without `(.venv)` in the prompt
- [ ] **12.** Compare the libraries — activated `pip list` vs deactivated `python3 -m pip list` (`.venv` list has `arcade`)
- [ ] **13.** Answer: why don't we just install arcade for the whole computer? (one sentence)

### Wrap-up (0.6)

- [ ] **14.** Confirm you can run a `.py` file from your editor or the terminal
- [ ] **15.** (Bonus, optional) Delete `.venv` and rebuild it with Fix B — proves `.venv` is disposable
