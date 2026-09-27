# Level 2: The Endless World

## Goal
The world scrolls **up**. The camera follows the player as they jump higher, and new platforms (plus the side walls) keep appearing above, so the climb seems endless. Left and right, walls stop the player. One constant, `MAX_HORIZONTAL`, is the farthest they can move sideways. The corner shows the height climbed.

## Concepts for the child
Cameras (world vs. screen), `while` loops, writing your own function, random numbers, and text on screen. The big idea: **"endless" is a trick. We build the world just before you see it** — this time, just above the player. One number the child picks decides the sideways limit.

## Key components

| Component | Responsibility | Arcade tool / idea |
|---|---|---|
| World camera | Follows the player upward; sideways, stays inside the shaft | `arcade.Camera2D()`, set `.position` each frame |
| GUI camera | Keeps the HUD fixed on screen | A second `Camera2D()` that never moves |
| Sideways limit | Maximal horizontal distance, chosen by the learner | `MAX_HORIZONTAL` (start at `10 * TILE_SIZE`). **TRY THIS** |
| Floor | A place to start the climb | One row of grass from x = 0 to `MAX_HORIZONTAL` |
| Side walls | Stop the player at the left and right edges | A column of boxes at each edge, grown upward with the world |
| Generation cursor | Remembers how high the next row goes | `next_y` and `next_platform_y` |
| World builder | Adds wall tiles and platforms until the cursor reaches a target y | Your own function `build_world_up_to(far_y)` with a `while` loop |
| Platforms | Somewhere to land on the way up | A short row of tiles inside the walls; rise of 1 or 2 tiles |
| Start safety | The first jump is easy | First platform is only 2 tiles above the floor |
| Height HUD | Shows meters climbed | `arcade.Text`, update `.text` each frame |

## Build steps
1. Copy Level 1 and remove the fixed boxes and the screen clamp. The walls, not the window edges, now stop the player.
2. Add the sideways limit and the cursors:
   ```
   MAX_HORIZONTAL = 10 * TILE_SIZE   # TRY THIS: smaller = a tighter shaft
   next_y = 0
   next_platform_y = 3 * TILE_SIZE    # first platform, 2 tiles above the floor
   ```
   Keep `MAX_HORIZONTAL` at least `6 * TILE_SIZE` so two walls and a platform still fit.
3. Add a floor across `0 .. MAX_HORIZONTAL`, then `build_world_up_to(far_y)`:
   ```
   while next_y < far_y:
       add a wall tile on the left and on the right at next_y
       if next_y == next_platform_y:
           pick a width of 2 to 4 tiles that fits between the walls
           pick a left edge inside the shaft, within 3 tiles of the previous platform
           add the platform tiles
           next_platform_y += TILE_SIZE * random.randint(1, 2)
       next_y += TILE_SIZE
   ```
4. Call it once at startup (2 screens of height), then every update with `player.center_y + 2 × WINDOW_HEIGHT`.
5. Add both cameras. In `on_draw`, use the world camera → draw world, then the GUI camera → draw text.
6. Camera position:
   - `y = max(player.center_y, WINDOW_HEIGHT/2)` so the climb scrolls and the floor stays on screen at the start.
   - Sideways, never show past the walls. If `MAX_HORIZONTAL` fits in the window, `x = MAX_HORIZONTAL/2`. If the learner makes it wider than the window, `x = min(max(player.center_x, WINDOW_WIDTH/2), MAX_HORIZONTAL - WINDOW_WIDTH/2)`.
7. Height text: `int((player.center_y - TILE_SIZE) / TILE_SIZE)`.

**Constraint:** each new platform rises by at most 2 tiles (128 px), because the jump reaches about 190 px. A rise of 3 tiles is right at the limit. The sideways gap from the previous platform stays within about 3 tiles, which is how far one jump carries the player. A very small `MAX_HORIZONTAL` forces platforms to nearly fill the shaft, so the climb is almost straight up.

## How to test

### Play test checklist
| Action | Expected |
|---|---|
| Jump upward for 30+ seconds | Platforms never run out, and no gaps or flicker at the top edge |
| Look at the HUD while climbing | Text stays in the corner and doesn't scroll away |
| Hold LEFT, then RIGHT | Each wall stops the player; they never pass `MAX_HORIZONTAL` |
| Change `MAX_HORIZONTAL` and restart | A smaller number pulls the walls in; a larger number gives more sideways room. Platforms still sit between the walls |
| Set `MAX_HORIZONTAL` wider than the window | Camera pans sideways with the player and never shows empty space past either wall |
| Restart the game several times | Platform layout is different each time |
| Climb the first few platforms | Every one can be reached in a jump from the one below |
| Fall back down after climbing | Earlier platforms and the floor are still there |

### Automated checks
- **World above:** after N updates of a jump rhythm, `next_y >= player.center_y + WINDOW_HEIGHT`.
- **Walls every row:** for each generated height, one tile sits at the left edge and one at `MAX_HORIZONTAL`.
- **Platforms stay inside:** every platform tile has `left >= TILE_SIZE` and `right <= MAX_HORIZONTAL - TILE_SIZE`.
- **Camera follows the climb:** `camera.position[1] == max(player.center_y, WINDOW_HEIGHT/2)`.
- **Sideways lock:** hold RIGHT for many frames → `player.right <= MAX_HORIZONTAL`. Hold LEFT → `player.left >= 0`.
- **Always climbable:** each platform is at most 2 tiles above the previous one, and the sideways gap is at most 3 tiles. With `random.seed(n)` for several n, an auto-climber (jump whenever `can_jump()`, steer toward the next platform) reaches y > 3000.
- **Safe start:** the first platform is exactly 2 tiles above the floor.
- **Performance (optional):** climb 10,000 px and check the frame time stays stable. This is a good time to discuss removing platforms far below the player.

## Done when
- [ ] Child can explain why the climb *seems* endless
- [ ] Child can say which things are drawn with which camera and why
- [ ] Child changed `MAX_HORIZONTAL` and saw the sideways range change
- [ ] Child changed the rise (`1` vs `2` tiles) and saw which climbs still work
