# Level 3: Coins and Floating Platforms

## Goal
The endless world now has floating platforms with coin rows on top and coins near the ground. Touching a coin removes it, adds 1 to the score, and plays a sound. The jump also makes a sound.

## Concepts for the child
Collision detection, counting with variables, removing things from the game, sounds, and `and` / `elif` in generation rules.

## Key components

| Component | Responsibility | Arcade tool / idea |
|---|---|---|
| Coin list | All coins | `SpriteList(use_spatial_hash=True)` |
| `add_coin(x, y)` | Helper that makes one coin | Your own function |
| `add_platform(start_x, width)` | A row of half-tiles plus a coin above each tile | `grassHalf_mid.png`; height from `random.choice([...])` |
| Platform spacing | Stops platforms from overlapping | `tiles_since_platform` counter |
| Generation rules | Decide per tile: platform, box, coin, or nothing | `if / elif / elif` with random chances |
| Coin collection | Detect touching coins and remove them | `arcade.check_for_collision_with_list(player, coins)`, `coin.remove_from_sprite_lists()` |
| Score + HUD | Count coins and show them | `self.score`, `arcade.Text` |
| Sounds | Feedback | `arcade.load_sound` once at the top, `arcade.play_sound` when the event happens |

## Build steps
1. Load the sounds once at the top of the file, not inside the loop.
2. Write `add_coin` and `add_platform`.
3. Extend `build_world_up_to` with this decision order:
   ```
   if in safe area and enough tiles since last platform and chance → platform
   elif in safe area and chance → box
   elif in safe area and chance → ground coin
   ```
4. In `on_update`, after physics: collect touched coins → remove each, add to score, play sound.
5. Play the jump sound inside the jump branch.
6. HUD: `Coins: {score}`.

**Height constraint:** a half-tile platform's top is at `center_y + 32`. The top must be ≤ ground top + about 180, so the center heights are {160, 200}. A center of 260 would be *unreachable*, which is a good bug to show kids.

## How to test

### Play test checklist
| Action | Expected |
|---|---|
| Touch a coin | It disappears, score +1, "ding" |
| Stand still on a coin spot | Score goes up only once |
| Jump | Jump sound plays, only when the jump actually happens |
| Reach every platform | Possible from the ground (or from a box) |
| Walk under a low platform | No head-bump that traps the player |
| Coins on platforms | Can be collected by jumping from the platform |

### Automated checks
- **Collect once:** put the player on a coin and run 10 updates → score increases by exactly 1 and the coin count decreases by 1.
- **Reachability:** for every platform, `platform.top - 64 <= MAX_JUMP` (measure MAX_JUMP in a test, about 190).
- **No overlap:** the horizontal ranges of any two platforms don't overlap.
- **Coins not inside walls:** for every coin, `get_sprites_at_point(coin.position, walls)` is empty.
- **Deterministic run:** with `random.seed(1)`, an auto-runner collects more than 0 coins in 600 frames.

## Done when
- [ ] Child can explain what a "collision" is
- [ ] Child can make coins worth 10 points
- [ ] Child found (or was shown) why a too-high platform can't be reached
