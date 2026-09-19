# Level 6: The Complete Game

## Goal
Turn the project into a finished game: a title screen, gameplay, and a game-over/win screen. The hero is animated (idle, walk, jump, fall, facing direction). Moving platforms, a pause key, a stage-clear bonus, and a high score that is saved to a file are added. The maps move into their own module, `stages.py`.

## Concepts for the child
Classes you write yourself (a `Player` that knows how to animate), screens (Views) and switching between them, animation as a flip book, `import` from your own file, reading and writing files, and `try/except`.

## Architecture

```
main:  Window → show TitleView
TitleView --SPACE--> GameView --lives 0 / last flag--> EndView
EndView  --R--> GameView       EndView --ESC--> TitleView
GameView --ESC--> TitleView
stages.py  → STAGES (data only)
highscore.txt  ← read by Title/End, written by End
```

## Key components

| Component | Responsibility | Arcade tool / idea |
|---|---|---|
| `stages.py` | All maps plus design rules in comments | Plain Python module, `from stages import STAGES` |
| `Player(arcade.Sprite)` | Loads textures and picks one each frame | `load_texture`, `.flip_left_right()` |
| Texture pairs | [facing right, facing left] for each pose | Loaded once to avoid work every frame |
| `animate(dt, on_ground)` | Picks idle / walk frame / jump / fall | Walk frame = `int(timer*12) % 8` |
| `TitleView` | Title, start hint, high score, demo walk | `arcade.View` |
| `GameView` | Level 5 logic moved into a View | `on_show_view` sets the background |
| `EndView(message, score)` | Result, new-record check, R/ESC | Saves the high score if beaten |
| Moving platforms `M` | Slide between two edges and carry the player | `platforms=` argument of the physics engine; `boundary_left/right`, `change_x` |
| Alternating direction | Neighbouring platforms move in opposite directions | Every 2nd `M` starts with negative `change_x` |
| Pause | Freeze updates, show "PAUSED" | A boolean toggled with `not` |
| High score I/O | Load and save an int | `open`, `int()`, `try/except (FileNotFoundError, ValueError)` |
| Save path | Stored next to the script | `os.path.dirname(os.path.abspath(__file__))` |
| Stage bonus | +10 × remaining lives | Added when the flag is touched |

## Build steps
1. **Refactor only:** move `STAGES` to `stages.py`, import it, and check the game plays exactly as in Level 5.
2. **Refactor only:** turn `GameWindow` into `GameView(arcade.View)`, create a plain `Window` in main, and show the view. Test again.
3. Add `EndView` and route game over / win to it. Remove the old message logic.
4. Add `TitleView` and the ESC route back to it.
5. High score functions, then show them on Title and End.
6. `Player` class with animation, and call `animate` after the physics update.
7. Moving platforms: new letter `M`, set boundaries and direction, pass them as `platforms=`. Design the "Moving Bridge" stage so that platforms *meet* each other (gaps ≤ 3 tiles at the closest point).
8. Pause and the stage bonus.

> Do the refactors in steps 1–2 with **no new features** and test after each one. This teaches a professional habit: change the structure, prove nothing broke, and only then add features.

## How to test

### Play test checklist
| Action | Expected |
|---|---|
| Launch | Title screen with the high score (0 the first time) |
| SPACE | Stage 1 starts |
| Walk / stop / jump / fall | Walking animation, idle when stopped, jump pose going up, fall pose coming down |
| Walk left | Hero faces left, and still faces left after stopping |
| Stand on a moving platform | Carried along without sliding off |
| Cross the Moving Bridge | Possible by waiting for the platforms to come close |
| P | Everything freezes and "PAUSED" shows; P again resumes |
| Lose all lives | End screen "GAME OVER" with score and high score |
| Beat the high score | "NEW HIGH SCORE!"; still there after quitting and relaunching |
| Delete `highscore.txt` or write "abc" in it | Game still starts, and the high score shows 0 |
| R / ESC on the end screen | New game / title screen |
| Add a 5th stage to `stages.py` | Appears automatically after stage 4 |

### Automated checks
- **Module:** `from stages import STAGES` works, and every stage passes the Level 5 map validator.
- **View flow:** send SPACE to the title view → `window.current_view` is a `GameView`. Force lives to 1 and cause a hit → it becomes an `EndView`.
- **Animation state:**
  - on ground with `change_x = 0` → the idle texture
  - `change_x > 0` over several frames → cycles through walk textures
  - in the air with `change_y > 0` → the jump texture
  - `change_x < 0` → the texture comes from the left-facing half of the pair
- **Moving platform ride:** put the player on the first `M` and run 30 frames → the player's x change equals the platform's x change (±1), and the player stays on top.
- **Opposite directions:** the `change_x` signs of the `M` platforms alternate (+, −, +).
- **High score I/O:**
  - no file → returns 0
  - "abc" in the file → returns 0
  - `save(40)` then load → returns 40
  - `EndView` with a lower score → the file is unchanged
- **Pause:** set `paused = True`, run 60 frames → player and enemy positions are unchanged.
- **Full run:** teleport onto each flag in turn → `EndView("YOU WIN!")` appears, and the score includes the life bonuses.

## Done when
- [ ] All screens are reachable and all routes between them work
- [ ] The high score persists between runs and survives a broken file
- [ ] The child added a stage in `stages.py` without touching the game code
- [ ] The child can explain what a View is and what `animate` decides
