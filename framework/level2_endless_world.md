# Level 2: The Endless World

## Goal
The world scrolls. The camera follows the player to the right, and ground (plus random box stacks) keeps appearing ahead, so the world seems endless. The top corner shows the distance walked.

## Concepts for the child
Cameras (world vs. screen), `while` loops, writing your own function, random numbers, and text on screen. The big idea: **"endless" is a trick. We build the world just before you see it.**

## Key components

| Component | Responsibility | Arcade tool / idea |
|---|---|---|
| World camera | Follows the player | `arcade.Camera2D()`, set `.position` each frame |
| GUI camera | Keeps the HUD fixed on screen | A second `Camera2D()` that never moves |
| Generation cursor | Remembers where the next tile goes | `next_tile_x` |
| World builder | Adds tiles until the cursor reaches a target x | Your own function `build_world_up_to(far_x)` with a `while` loop |
| Random obstacles | Occasional box stacks | `random.random() < BOX_CHANCE`, `random.randint(1, 2)` |
| Start safety zone | Keeps obstacles away from the spawn point | Only place obstacles when `x > 400` |
| Left wall | Stops the player walking into emptiness | A column of boxes at x < 0 |
| Distance HUD | Shows meters walked | `arcade.Text`, update `.text` each frame |

## Build steps
1. Copy Level 1 and remove the fixed boxes and the screen clamp.
2. Add `next_tile_x = 0` and the `build_world_up_to(far_x)` function:
   ```
   while next_tile_x < far_x:
       add grass at next_tile_x
       maybe add a box stack (not near the start)
       next_tile_x += TILE_SIZE
   ```
3. Call it once at startup (2 screens' worth), then every update with `player.center_x + 2 × WINDOW_WIDTH`.
4. Add the left boundary wall.
5. Add both cameras. In `on_draw`, use the world camera → draw world, then the GUI camera → draw text.
6. Camera position: `x = max(player.center_x, WINDOW_WIDTH/2)`, `y = WINDOW_HEIGHT/2`.
7. Distance text: `int(player.center_x / TILE_SIZE)`.

**Constraint:** box stacks must stay at 2 or fewer (128 px), because the jump reaches about 190 px. Stacks of 3 are right at the limit.

## How to test

### Play test checklist
| Action | Expected |
|---|---|
| Walk right for 30+ seconds | Ground never runs out, and no gaps or flicker at the far edge |
| Look at the HUD while walking | Text stays in the corner and doesn't scroll away |
| Walk left at the start | Wall stops the player; camera never shows empty space on the left |
| Restart the game several times | Box layout is different each time |
| Meet every box stack | All can be jumped over |
| Walk back left after going far | Ground is still there |

### Automated checks
- **Ground ahead:** after N updates holding RIGHT, `next_tile_x >= player.center_x + WINDOW_WIDTH`.
- **No holes:** collect the `left` values of all grass tiles, sort them, and check each difference is exactly `TILE_SIZE`.
- **Camera follows:** `camera.position[0] == max(player.center_x, WINDOW_WIDTH/2)`.
- **Safe start:** no boxes with `left < 400`.
- **Always jumpable:** the tallest stack is ≤ 2 tiles. With `random.seed(n)` for several n, an auto-runner (hold RIGHT, jump every 20 frames) reaches x > 3000.
- **Performance (optional):** walk 10,000 px and check the frame time stays stable. This is a good time to discuss removing tiles far behind the player.

## Done when
- [ ] Child can explain why the world *seems* endless
- [ ] Child can say which things are drawn with which camera and why
- [ ] Child changed `BOX_CHANCE` and saw the result
