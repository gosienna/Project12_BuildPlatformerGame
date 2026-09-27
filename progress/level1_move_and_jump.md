# Level 1: Move and Jump — progress

Learner: kw
Branch: kw
Source plan: `framework/level1_move_and_jump.md`

Progress: **bite T5b1 of ~39** — waiting to create a new `.venv` folder

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
- [x] **T2.** Add `ENV_TAG` so the title reads `Platformer (.venv)`; confirm with `which python`
- [x] **7.** Create the player sprite at a start position and draw it
- [x] **8a.** `TILE_SIZE` + one grass tile on a new `wall_list` and draw it (`use_spatial_hash=True` already present; revisit in 8c)
- [x] **8b.** `for` loop with `range(..., TILE_SIZE)` to fill a full ground row
- [x] **8c.** `use_spatial_hash=True` on `wall_list` (same look; ready for physics later)
- [x] **T3a.** `deactivate`, then `python3 level1.py` — `No module named 'arcade'`
- [x] **T3b.** Activate again and run — game + `(.venv)` title back
- [x] **T3c.** Run `.venv/bin/python level1.py` without activating — window still opens; `arcade` lives inside `.venv`
- [x] **9a.** One box sprite on `wall_list`, sitting on the grass
- [x] **9b.** A list of `(x, y)` positions and a `for` loop that places the rest of the boxes
- [x] **10a.** `on_update` prints `delta_time` each frame — numbers around 0.017
- [x] **10a-tune.** `set_update_rate(1/30)` printed about 0.034; rate `1` printed about 1.0; set back to `1/60` and removed the print
- [x] **10b.** Physics engine calls `update()` — character falls onto the grass (`gravity_constant` is `0.1` for now; set back to `1` in 10c)
- [x] **10c.** `gravity_constant` 0.3 falls slowly, 2 falls fast, then set back to `1`
- [x] **11a.** `on_key_press` prints the key number — character still does not walk
- [x] **11a-left.** `if` the key is LEFT, set `left_pressed = True` and print it
- [x] **11a-right.** Same pattern for `right_pressed`
- [x] **11a-release.** `on_key_release` sets the matching flag back to `False`
- [x] **11b.** In `on_update`, set `change_x` from flags — walks left and right, stops when released
- [x] **11b-tune.** `PLAYER_SPEED` 2 is slow, 12 is fast, then set back to `5`
- [x] **11c.** Jump: only if `can_jump()`, set `change_y = JUMP_POWER`
- [x] **11c-tune.** `JUMP_POWER` 8 is a short hop, 35 is a high jump, then set back to `20`
- [x] **12.** Clamp the player to the window edges after physics update
- [x] **13.** TRY THIS notes on speed, jump, and gravity; speed set back to `5`
- [x] **T4a.** `ls .venv` shows `bin`; the toolbox list includes `python`, `pip`, `activate`, `Activate.ps1`, and `activate.fish`
- [x] **T4b.** `pip list` — `arcade` 3.3.3 is in the short list
- [x] **T4c.** `pip show arcade` — `Location` is inside `.venv`; the toolbox keeps this project separate from the rest of the computer
- [x] **T5a.** Deleted `.venv` — `python3 level1.py` raises `No module named 'arcade'`; `level1.py` stayed
- [ ] **T5b1.** `python3 -m venv .venv` — the `.venv` folder exists again
- [ ] **T5b2.** `source .venv/bin/activate` — the prompt starts with `(.venv)`
- [ ] **T5b3.** `pip install arcade`, then run the game — the window opens and `level1.py` was never changed
- [ ] **14.** Create `game/`, move `level1.py` into it, and run `python game/level1.py` once — the window from that file is the start of the game
- [ ] **15.** Start `.venv/bin/python .cursor/skills/instructor/scripts/watch_game.py`; saving any `.py` inside `game/` reopens the window; stop with `Ctrl+C`
- [ ] **16.** Save a drawing or web image as `game/hero.png`, point the player sprite at `"game/hero.png"`, and save `game/level1.py` — the watcher reopens the window with that picture as the hero; grass and boxes stay on `:resources:` images
