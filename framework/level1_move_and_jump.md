# Level 1: Move and Jump

## Goal
A single, fixed screen with ground and a few boxes. The player walks left and right and jumps. They can land on boxes but can't jump in mid-air or leave the screen.

## Concepts for the child
Variables and constants, the x/y coordinate system (y = 0 is at the **bottom**), `import`, the `if` statement, `for` loops, True/False, and the game loop.

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

## Build steps (instructor bites)

Prerequisite: **[Level 0 setup check](level0_setup.md) passed** (Python 3.10+, Arcade 3.x, window opens).

Progress: **waiting for user to create `level1.py`** → then bite 1 (empty window)

- [ ] **1.** Open an empty window with a background color and check that it runs.
- [ ] **2.** Create the player sprite at a start position and draw it.
- [ ] **3.** Build the ground row with a loop and draw it.
- [ ] **4.** Add the boxes from a list of positions.
- [ ] **5.** Create the physics engine and call `physics_engine.update()` in `on_update`.
- [ ] **6a.** Keyboard flags: on press/release set/clear `left_pressed` / `right_pressed`.
- [ ] **6b.** In `on_update`, set `change_x` from flags (`0`, then `-SPEED` / `+SPEED`).
- [ ] **6c.** Jump: on jump key, **only if** `can_jump()`, set `change_y = JUMP_POWER`.
- [ ] **7.** Clamp the player to the window edges after the physics update.
- [ ] **8.** Add "TRY THIS" comments that point at the tunable constants.

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

### Automated checks
- **Lands on ground:** run 120 updates → `can_jump()` is True and `player.bottom ≈ 64`.
- **Walks:** press RIGHT, run 60 updates → `center_x` increased by about `60 × SPEED`.
- **No air jump:** jump, run 5 updates, press jump again → `change_y` is not reset to `JUMP_POWER`.
- **Bounds:** hold RIGHT for 600 updates → `player.right <= WINDOW_WIDTH`.
- **Jump height:** record the highest `player.bottom` during one jump → about 190 px above the ground.

### Tuning experiments (the child records the results)
Double `JUMP_POWER`, halve `GRAVITY`, and so on, and describe how it *feels*. This teaches that one number changes the whole feel of the game.

## Done when
- [ ] All play-test rows pass
- [ ] Child can point to where the player is created, drawn, and moved
- [ ] Child has changed at least 2 constants and explained the effect
