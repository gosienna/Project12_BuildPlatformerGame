# Platformer Tutorial: Design Framework (Overview)

This folder describes **what to build and how to check it** for each tutorial level, without the full code. Each level file has the same five parts:

1. **Goal**: what the child can do when the level is finished
2. **Key components**: the building blocks and which Arcade tool does each job
3. **Build steps**: the order to build it in, written as plain steps or pseudocode
4. **How to test**: a hands-on play checklist plus automated checks
5. **Done when**: the checklist for moving on

Target: Python Arcade 3.x (Python 3.10+). Art and sounds come from Arcade's built-in `:resources:` library.

**Start with [Level 0: Quick Setup Check](level0_setup.md).** It takes about 5 minutes. It only checks that Python 3.10+ and Arcade are installed and that a window opens, and gives the matching fix if not. The `.venv` and the terminal are taught in Level 1, once a game is running and each command gives a visible result.

## Dependency rule: one install only

The only thing a child ever installs is **`arcade`** (`pip install arcade`). Arcade brings its own dependencies automatically.

- **Allowed:** `arcade` and Python's standard library (`random`, `os`, `sys`, `math`). These need no installing.
- **Not allowed:** any other `pip install` (numpy, matplotlib, pillow, pygame, pytest and so on). If a level seems to need one, do it with plain Python or with an Arcade feature instead.
- **Tests:** plain scripts using `assert`. No pytest or other test framework. `xvfb-run` (Linux only, teachers only) is a system program, not a Python package.
- **Save files (Level 6):** a plain text file using built-in `open()` and `int()`. No extra module is needed.
- **Art and sound:** use Arcade's built-in `:resources:` only. Don't ask the child to download assets.
- **Adding a level:** list any new import in that level's "Key components" table, and it must be `arcade` or standard library.

## Progression at a glance

| Level | Theme | Builds on | Main new concepts |
|---|---|---|---|
| 0 | Quick Setup Check (5 min) | nothing | none (copy the commands) |
| 1 | Move & Jump | L0 | window, sprite, game loop, keyboard, gravity, **terminal, `.venv`** |
| 2 | Endless World | L1 | camera, procedural generation, random, HUD text |
| 3 | Coins & Platforms | L2 | collision, score, sound, generation rules |
| 4 | Danger! | L3 | lives, respawn, invincibility timer, enemies, reset/restart |
| 5 | Level Designer | L4 (non-random) | text maps, stage progression, enemy edge detection |
| 6 | Complete Game | L5 | Views (screens), animation, moving platforms, save file, modules |

## The skeleton every level shares

Keep this layout in every level so children always know where to look:

```
SETTINGS (CAPITAL constants: sizes, speeds, picture paths)
class GameWindow / GameView
    __init__      → build things once
    setup()       → (from L4) reset everything for a new game
    on_draw       → clear, draw lists (world camera), draw HUD (gui camera)
    on_update     → move, physics, collisions, camera, HUD text
    on_key_press / on_key_release → set flags, jump
run the game
```

Mark every new line in a level with `# NEW` so children can compare levels side by side.

## Shared physics numbers (keep them the same across levels)

| Setting | Value | Effect |
|---|---|---|
| `TILE_SIZE` | 64 px | Built-in tiles at `scale=0.5` |
| `GRAVITY` | 1 | Pixels per frame² |
| `JUMP_POWER` | 20 | Maximum jump height is about **190 px (just under 3 tiles)** |
| `PLAYER_SPEED` | 5–6 | Covers about **3.5 tiles** horizontally in one jump |

**Design rule for levels:** platforms can be at most **2 tiles** higher than where the player stands, and gaps at most **3 tiles** wide. Every level design must respect this rule, or some parts can't be reached.

## Common testing strategy (applies to every level)

**A. Play test (manual):** a checklist of "do X, expect Y". Children can do this themselves, and it teaches them to test like game developers.

**B. Headless automated test (for the adult or teacher):** run the game without a real screen and "press keys" in code.

```
create the window/view
call on_key_press(RIGHT)
repeat N times: on_update(1/60)
assert something about player / score / lives
optionally: on_draw(); arcade.get_image().save("shot.png")
```

On Linux or CI, run it with `xvfb-run -a python test_levelX.py`. Calling `on_update` directly lets you run the game faster than real time and makes every test repeatable.

**C. Scenario setup:** put the player *directly* into a situation to test it. For example, place the player just above an enemy with `change_y = -5` and check the stomp. This is much more reliable than trying to play your way into that moment.

**D. Randomness:** for levels 2 to 4, call `random.seed(1)` in tests so the generated world is the same every run.
