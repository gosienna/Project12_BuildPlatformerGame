# Level 1: Move and Jump

## Goal
A single, fixed screen with ground and a few boxes. The player walks left and right and jumps. They can land on boxes but can't jump in mid-air or leave the screen.

## Concepts for the child
Variables and constants, the x/y coordinate system (y = 0 is at the **bottom**), `import`, the `if` statement, `for` loops, True/False, and the game loop.

Along the way, the child also learns the **terminal** and the **`.venv`** through short "terminal quests" (marked **T1** to **T5** below). Each quest comes right after a step where the game already runs, so every command gives a visible result: a window opens, a colour changes, a title changes, or the window fails to appear.

## Key components

| Component | Responsibility | Arcade tool |
|---|---|---|
| Settings block | Window size, speeds, jump power, gravity, picture paths | Plain constants |
| Game window | Owns everything and runs the loop | `arcade.Window` subclass |
| Player sprite | The hero picture and its position | `arcade.Sprite(path, scale=0.5)` |
| Sprite lists | Groups of sprites to draw and check together | `arcade.SpriteList()`; walls use `use_spatial_hash=True` |
| Ground | A row of grass tiles along the bottom | A `for x in range(...)` loop |
| Boxes | A few (x, y) positions stored in a list | A list of tuples |
| Physics engine | Gravity, landing, bumping into walls | `arcade.PhysicsEnginePlatformer(player, walls=..., gravity_constant=...)` |
| Input state | Which arrow keys are currently held | `left_pressed` / `right_pressed` booleans |
| Screen bounds | Keeps the player inside the window | Clamp `player.left` / `player.right` |
| Terminal | Starts the game, stops it, and shows errors | `cd`, `ls`, `python level1.py`, `Ctrl+C`, `↑` |
| `.venv` (private toolbox) | Holds this project's Python and `arcade` | `activate`, `deactivate`, `which python`, `pip list` |
| Environment label | Window title shows which Python is running | `sys.prefix != sys.base_prefix` (see T2) |

## Build steps (instructor bites)

Prerequisite: **[Level 0 quick check](level0_setup.md) passed** (Python 3.10+, Arcade 3.x, a window opened).

Progress: **waiting for user to create `level1.py`** → then bite 1 (empty window)

Terminal quests (**T1 to T5**) sit between the game bites. **Pacing rule:** the instructor gives one command at a time, asks the child to *predict* what will happen, then they run it. Each quest takes about 3 minutes. Windows equivalents are in brackets.

- [ ] **1.** Open an empty window with a background color and check that it runs.
- [ ] **T1. The run loop** (window is open, so the effect is visible)
  1. `pwd` [`cd`] shows the folder the terminal is standing in. `ls` [`dir`] shows `level1.py` in it.
  2. `python level1.py` opens the window. Close it with the X button, then run it again and stop it with `Ctrl+C` in the terminal instead.
  3. Change the background color in the editor and **save**. In the terminal press `↑` then `Enter` (the last command comes back), and the window returns in the new color.
  4. Repeat with 3 colors. The child now has the **edit → save → run** loop.
- [ ] **T2. Which Python opened this window?** Add the label below, so the window title shows the answer.
  ```python
  import sys                                                        # NEW
  ENV_TAG = ".venv" if sys.prefix != sys.base_prefix else "system Python"   # NEW
  # ... in __init__:
  super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, f"Platformer ({ENV_TAG})")  # NEW
  ```
  Treat the two lines as a magic label for now. Run the game, and the title bar reads **Platformer (.venv)**. Then `which python` [`where python`] shows a path ending in `.venv/bin/python` [`.venv\Scripts\python.exe`]. That is the Python that opened the window.
- [ ] **2.** Create the player sprite at a start position and draw it.
- [ ] **3.** Build the ground row with a loop and draw it.
- [ ] **T3. Turn the toolbox off** (the game is now worth protecting)
  1. Type `deactivate`. The `(.venv)` in the prompt disappears.
  2. `python3 level1.py`. **Usually the window never appears** and the terminal says `No module named 'arcade'`. (If the computer has arcade installed globally, the title says "system Python" instead.)
  3. Activate again (`source .venv/bin/activate` [`.venv\Scripts\activate`]) and run it. The game and the `(.venv)` title are back.
  4. Now run `.venv/bin/python level1.py` [`.venv\Scripts\python level1.py`] **without activating**. It still works, and the title still says `.venv`. Lesson: "activate" only changes which `python` the terminal finds first.
  5. Ask: *"Where does arcade live?"* Answer: inside `.venv`. That is why `.venv` exists: **a private toolbox for one project**.
- [ ] **4.** Add the boxes from a list of positions.
- [ ] **5.** Create the physics engine and call `physics_engine.update()` in `on_update`.
- [ ] **6a.** Keyboard flags: on press/release set/clear `left_pressed` / `right_pressed`.
- [ ] **6b.** In `on_update`, set `change_x` from flags (`0`, then `-SPEED` / `+SPEED`).
- [ ] **6c.** Jump: on jump key, **only if** `can_jump()`, set `change_y = JUMP_POWER`.
- [ ] **7.** Clamp the player to the window edges after the physics update.
- [ ] **8.** Add "TRY THIS" comments that point at the tunable constants. The child changes a constant, saves, and uses `↑` + `Enter` to re-run (the T1 loop) to see the effect at once.
- [ ] **T4. Peek inside the toolbox** (a finished game to look after)
  1. `ls .venv/bin` [`dir .venv\Scripts`] shows `python`, `pip` and `activate`. `.venv` is just a folder.
  2. `pip list` shows a short list including `arcade`. (Arcade brings its own helpers, and that's fine.)
  3. `pip show arcade` has a `Location:` line that points **inside `.venv`**.
  4. Ask: *"Why not install arcade for the whole computer?"* A good answer: other projects may need other versions, and a mistake stays inside one folder that can be deleted.
- [ ] **T5. Bonus: break it and rebuild it.**
  1. `deactivate`, then `rm -rf .venv` [`rmdir /s /q .venv`]. Run the game: it fails, so the window is gone.
  2. Rebuild with the three **Fix B** commands from Level 0. Run the game: the window is back, and `level1.py` was never touched. `.venv` is disposable and the project files are safe.

> Why use flags instead of setting `change_x` directly in `on_key_press`? If you do it directly, then holding RIGHT, tapping LEFT and releasing it stops the player even though RIGHT is still held. Flags avoid that bug.

## How to test

### Play test checklist
| Action | Expected |
|---|---|
| Start the game | Player falls and lands on the grass, not through it |
| Hold RIGHT | Walks smoothly to the right edge and stops there |
| Hold LEFT | Walks to the left edge and stops there |
| Press SPACE on the ground | Jumps and comes back down |
| Press SPACE many times in the air | No extra jumps |
| Hold RIGHT, tap LEFT and release it | Player keeps walking right |
| Jump onto a box | Lands and stands on top |
| Walk into a box | Blocked from the side |
| Reach the highest box via the others | Possible (checks the level can be completed) |
| Edit a color, save, press `↑` `Enter` | The window reopens with the new color (T1) |
| Look at the title bar | Reads `Platformer (.venv)` (T2) |
| `deactivate`, then run with `python3` | No window, and a `No module named 'arcade'` error (T3) |
| Run `.venv/bin/python level1.py` without activating | The game opens, and the title says `.venv` (T3) |

### Automated checks
- **Lands on ground:** run 120 updates → `can_jump()` is True and `player.bottom ≈ 64`.
- **Walks:** press RIGHT, run 60 updates → `center_x` increased by about `60 × SPEED`.
- **No air jump:** jump, run 5 updates, press jump again → `change_y` is not reset to `JUMP_POWER`.
- **Bounds:** hold RIGHT for 600 updates → `player.right <= WINDOW_WIDTH`.
- **Jump height:** record the highest `player.bottom` during one jump → about 190 px above the ground.
- **Runs in the venv:** `.venv/bin/python -c "import sys; assert sys.prefix != sys.base_prefix"` exits with code 0. The same command with the system `python3` must fail.

### Tuning experiments (the child records the results)
Double `JUMP_POWER`, halve `GRAVITY`, and so on, and describe how it *feels*. This teaches that one number changes the whole feel of the game.

## Done when
- [ ] All play-test rows pass
- [ ] Child can point to where the player is created, drawn, and moved
- [ ] Child has changed at least 2 constants and explained the effect
- [ ] Child can start and stop the game from the terminal, and re-run it with `↑` + `Enter`
- [ ] Child can say in one sentence what `.venv` is for, and has seen the game fail without it (T3)
- [ ] Child can use `pwd`, `ls`, `cd`, `activate` and `deactivate` without help
