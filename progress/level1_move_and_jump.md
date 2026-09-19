# Level 1: Move and Jump — progress

Learner: kw
Branch: kw
Source plan: `framework/level1_move_and_jump.md`

Progress: **bite 1 of 18** — waiting for learner to create `level1.py`

## Bites

### Game + terminal quests

- [ ] **1.** Open an empty window with a background color and check that it runs
- [ ] **T1a.** `pwd` then `ls` — see `level1.py` in the project folder
- [ ] **T1b.** Run `python level1.py`; close with X, then stop with `Ctrl+C`
- [ ] **T1c.** Change background color, save, re-run with `↑` + `Enter` (try 3 colors)
- [ ] **T2.** Add `ENV_TAG` so the title reads `Platformer (.venv)`; confirm with `which python`
- [ ] **2.** Create the player sprite at a start position and draw it
- [ ] **3.** Build the ground row with a loop and draw it
- [ ] **T3a.** `deactivate`, then `python3 level1.py` — usually no window / no arcade
- [ ] **T3b.** Activate again and run — game + `(.venv)` title back
- [ ] **T3c.** Run `.venv/bin/python level1.py` without activating — still works; say where arcade lives
- [ ] **4.** Add the boxes from a list of positions
- [ ] **5.** Create the physics engine and call `physics_engine.update()` in `on_update`
- [ ] **6a.** Keyboard flags: press/release set/clear `left_pressed` / `right_pressed`
- [ ] **6b.** In `on_update`, set `change_x` from flags
- [ ] **6c.** Jump: only if `can_jump()`, set `change_y = JUMP_POWER`
- [ ] **7.** Clamp the player to the window edges after physics update
- [ ] **8.** Add "TRY THIS" comments; change a constant, save, re-run with `↑` + `Enter`
- [ ] **T4.** Peek inside the toolbox (`ls .venv/bin`, `pip list`, `pip show arcade`) + why not install globally
- [ ] **T5.** (Bonus) Delete `.venv`, see the game fail, rebuild with Fix B
