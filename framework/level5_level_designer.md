# Level 5: Be the Level Designer!

## Goal
Stop generating the world randomly. Instead, **draw** each stage as rows of letters. There are several stages, each with a name. Touching the flag loads the next stage, and after the last one the game shows "YOU WIN!". Spikes are added, and slimes become smarter: they turn around at edges and walls on their own.

## Concepts for the child
Lists of strings as a 2D grid, `enumerate` (row and column numbers), dictionaries (letter → picture), turning a row number into a y position, and simple AI ("look before you step").

## Map format

```
.  sky        =  ground      -  floating platform   B  box
C  coin       E  slime       ^  spikes              F  flag      P  start
```
- Each stage is `{"name": "...", "map": [row0, row1, ...]}`, with **row 0 at the top**.
- Exactly one `P`, and at least one `F`.
- Reachability: at most 2 tiles up and 3 tiles across per jump.

## Key components

| Component | Responsibility | Idea |
|---|---|---|
| `STAGES` | List of stage dictionaries | Data, not code, so kids edit this part |
| Letter table | Letter → (picture, which list) | A dictionary |
| `load_stage()` | Turns the text into sprites | Two nested `enumerate` loops |
| Grid → pixels | Position of each tile | `x = col*64 + 32`; `y = (rows-1-row)*64 + 32` |
| World width | For the camera limits | `max(len(row)) * 64` |
| `new_game()` | Lives, score, stage 0 → `load_stage()` | Replaces `setup()` |
| Respawn | Go back to `P` of the current stage | Replaces the "safe spot" from L4 |
| Spikes | Hurt on any touch | Collision list check |
| Flag | Next stage or win | `stage_number += 1`; compare with `len(STAGES)` |
| Smart slime | Turn around at a wall ahead or no ground ahead | `get_sprites_at_point((front_x, …), walls)` |
| Clamped camera | Never shows past the world edges | `min(max(x, half), world_width - half)` |
| Message state | "GAME OVER" / "YOU WIN!" | One `message` string; empty means playing |

## Build steps
1. Write a tiny stage 1 by hand (just `P`, ground, `F`) and write `load_stage()`. Check the positions look right.
2. Add the other letters one at a time and look at the result after each.
3. Flag → next stage → win message.
4. Replace the Level 4 patrol with look-ahead: check a point just past the slime's front edge, (a) at body height for walls and (b) just below its feet for ground.
5. Spikes and the respawn-at-P logic.
6. Clamp the camera to the world width.
7. Design stages 2 and 3 on a grid (squared paper first!), then check them against the reachability rules.

## How to test

### Map validation (run automatically before playing)
For every stage:
- Exactly one `P`, and at least one `F`.
- Only allowed letters appear.
- The world is at least one window wide (otherwise the camera clamp breaks).
- `F` and `E` have a solid tile directly beneath them.
- No pit is wider than 3 tiles (scan the bottom row for runs of `.`).
- Every `-` platform is ≤ 2 tiles above some surface within 3 columns (rough reachability check).

### Play test checklist
| Action | Expected |
|---|---|
| Start | Player appears at `P`; the map looks like the text |
| Touch the flag | Next stage loads; lives and score are kept |
| Touch the last flag | YOU WIN! is shown; R restarts at stage 1 |
| Touch spikes | Lose a life, back to `P`, blink |
| Watch a slime near a hole or box | It turns around and never walks into the air |
| Walk to both ends of the world | Camera stops at the edges; player can't leave the world |
| Edit a letter in the map and rerun | The change appears in the game |

### Automated checks
- **Grid mapping:** with a 3-row test map, `P` at (row 1, column 2) gives the start `(160, 96)`.
- **Flag progression:** teleport the player onto the flag each frame → `stage_number` counts up to `len(STAGES)`, then the message is "YOU WIN!".
- **Enemy stays grounded:** run 1200 frames; every slime's x stays within its ground segment.
- **Clamp:** player at x = 0 → camera x == WINDOW_WIDTH/2; player at the world end → camera x == world_width − WINDOW_WIDTH/2.
- **Completable (advanced):** a simple script that replays recorded key presses (a "ghost run") can finish each stage. Record one by playing, then replay it after every change.

## Done when
- [ ] The child has designed and finished their own stage
- [ ] The map validator passes for all stages
- [ ] The child can explain why row 0 ends up at the *top*
