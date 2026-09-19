# Level 1: Move and Jump — progress

Learner: kw
Branch: kw
Source plan: `framework/level1_move_and_jump.md`

Progress: **T2 of 23** — waiting for Platformer (.venv) in the title bar

## Bites

### Grow `level1.py` (one component at a time)

- [x] **1.** `def main()` that `print`s a message, then call `main()` — message appears in the terminal
- [x] **2.** Inside `main()`: `import arcade`, open `arcade.Window(...)`, call `arcade.run()` — a window opens (no class yet)
- [x] **3.** Wrap in `class GameWindow(arcade.Window)` with `__init__` + `super().__init__(...)`; `main()` creates `GameWindow()` — window still opens; `print` in `__init__` proves the class ran
- [x] **4.** Replace magic numbers with `WINDOW_WIDTH`, `WINDOW_HEIGHT`, `WINDOW_TITLE` — change a constant and the window size or title changes
- [x] **5.** Set `self.background_color` in `__init__` — window fills with a color
- [x] **6.** Add `on_draw` with `self.clear()` — colored window still draws cleanly each frame

### Terminal quests + rest of the level

- [x] **T1a.** `pwd` then `ls` — see `level1.py` in the project folder
- [x] **T1b.** Run `python level1.py`; close with X, then stop with `Ctrl+C`
- [x] **T1c.** Change background color, save, re-run with `↑` + `Enter` (try 3 colors)
- [ ] **T2.** Add `ENV_TAG` so the title reads `Platformer (.venv)`; confirm with `which python`
- [ ] **7.** Create the player sprite at a start position and draw it
- [ ] **8.** Build the ground row with a loop and draw it
- [ ] **T3a.** `deactivate`, then `python3 level1.py` — usually no window / no arcade
- [ ] **T3b.** Activate again and run — game + `(.venv)` title back
- [ ] **T3c.** Run `.venv/bin/python level1.py` without activating — still works; say where arcade lives
- [ ] **9.** Add the boxes from a list of positions
- [ ] **10.** Create the physics engine and call `physics_engine.update()` in `on_update`
- [ ] **11a.** Keyboard flags: press/release set/clear `left_pressed` / `right_pressed`
- [ ] **11b.** In `on_update`, set `change_x` from flags
- [ ] **11c.** Jump: only if `can_jump()`, set `change_y = JUMP_POWER`
- [ ] **12.** Clamp the player to the window edges after physics update
- [ ] **13.** Add "TRY THIS" comments; change a constant, save, re-run with `↑` + `Enter`
- [ ] **T4.** Peek inside the toolbox (`ls .venv/bin`, `pip list`, `pip show arcade`) + why not install globally
- [ ] **T5.** (Bonus) Delete `.venv`, see the game fail, rebuild with Fix B
