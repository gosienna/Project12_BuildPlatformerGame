# Level 4: Danger! Pits and Enemies

## Goal
Add ways to fail. There are holes in the ground and slimes walking back and forth. Landing on a slime from above squashes it (+5 points); touching it from the side costs a life. After getting hurt, the player respawns at the last safe spot and blinks, safe from harm, for 2 seconds. At 0 lives it's GAME OVER, and R restarts.

## Concepts for the child
Game states (playing / game over), resetting with `setup()`, countdown timers using `delta_time`, adding your own values to objects (`enemy.home_x`), and combining conditions (`falling and above`).

## Key components

| Component | Responsibility | Idea |
|---|---|---|
| `setup()` | Rebuilds everything for a new game | Moved out of `__init__`; `__init__` keeps only one-time things (cameras, text) |
| Game state | `lives`, `score`, `game_over` | `on_update` returns early when the game is over |
| Pits | Gaps in the generated ground | `pit_tiles_left` counter; only after enough flat ground |
| Flat-ground tracker | Makes sure slimes have room to walk | `flat_ground` counter, reset by pits and boxes |
| Enemy | Slime with a patrol range | `enemy.home_x`, `change_x`; turns around after walking `ENEMY_WALK_DISTANCE` |
| Facing | Slime looks the way it walks | `scale_x = ±0.5` |
| Safe spot | Where to respawn | Save the player's position whenever `can_jump()` is True |
| `lose_a_life()` | Hurt handler | lives −1 → game over, or respawn plus `safe_timer = SAFE_TIME` |
| Invincibility | Prevents losing several lives at once | While `safe_timer > 0`: blink with `alpha`, skip enemy checks |
| Stomp rule | Squash vs. get hurt | `change_y < 0` **and** `player.bottom > enemy.bottom + 5` |
| Fall-out | Falling into a hole | `player.top < -100` → lose a life |
| Game-over overlay | Big text plus restart hint | Drawn with the GUI camera when `game_over` |

## Build steps
1. Refactor: split `__init__` into one-time setup and `setup()`. Test that the game still works before adding anything new.
2. Add lives and the HUD (`Lives / Score / Distance`).
3. Pits in the generator. Keep them 1 to 2 tiles wide, never in the safe start area.
4. Fall detection → `lose_a_life()` → respawn at the safe spot.
5. Enemies: spawn only on flat ground (`flat_ground > 3`), then patrol *backwards* over the ground already built.
6. Enemy collision with the stomp rule. After one hit, `break` so the player doesn't lose several lives in the same frame.
7. Safe timer countdown and blinking.
8. Game over state, overlay, and R key → `setup()`.

**Pitfall to teach:** the first version of the stomp check used `bottom > enemy.center_y - 10`. At normal falling speed the player moves about 11 px per frame and skips past that small window, so stomps failed. Comparing *feet to feet* (`enemy.bottom + 5`) is both more forgiving and more reliable.

## How to test

### Play test checklist
| Action | Expected |
|---|---|
| Walk into a hole | Lose 1 life, reappear on the ground nearby, blink |
| Walk into a slime | Lose 1 life, blink, and the same slime doesn't hurt again right away |
| Jump onto a slime | Slime disappears, +5, player bounces |
| Stay near slimes while blinking | No damage |
| Lose all lives | GAME OVER text; the world stops moving |
| Press R after game over | Fresh game: 3 lives, score 0, new world |
| Press R during play | Nothing happens |
| Every hole | Can be jumped over (≤ 2 tiles) |
| Slimes | Never walk over holes or through boxes |

### Automated checks (scenario setup)
- **Stomp:** put the player 40 px above a slime with `change_y = -5`, run 10 frames → enemies −1, score +5, lives unchanged.
- **Side hit:** put the player on the ground overlapping a slime, run 1 frame → lives −1, `safe_timer == SAFE_TIME`.
- **Invincible:** straight after a side hit, run 30 frames still overlapping → lives unchanged.
- **Fall:** set `player.center_y = -500`, run 1 frame → lives −1 and the player is back at the safe spot.
- **Game over freezes:** set lives = 1, cause a hit, record the player position, run 60 frames → position unchanged.
- **Restart:** call `setup()` → lives == START_LIVES, score == 0, `game_over` is False.
- **Generator safety:** over 5 seeds, all pits are ≤ 2 tiles wide and every slime's patrol range lies on ground tiles.

## Done when
- [ ] Every row above passes
- [ ] Child can explain why we need `setup()`
- [ ] Child can explain the stomp rule in their own words
