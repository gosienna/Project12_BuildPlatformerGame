# Level 2: The Endless World — progress

Learner: kw
Branch: kw
Source plan: `framework/level2_endless_world.md`

Progress: **bite 1 of 28** — waiting for `game/level2.py`

## Bites

- [ ] **1.** Copy `game/level1.py` to `game/level2.py` and set the window title to `Endless` — the title bar shows `Endless (.venv)`
- [ ] **2.** Remove the box crates — only grass and the hero remain
- [ ] **3.** Remove the left/right window clamp — the hero can walk off the side of the screen
- [ ] **4.** `MAX_HORIZONTAL = 10 * TILE_SIZE` and the grass row uses it — the floor stops short of the right edge
- [ ] **5.** Tune `MAX_HORIZONTAL`: `6 * TILE_SIZE` is a shorter floor, `12 * TILE_SIZE` almost reaches the right edge, then set back to `10 * TILE_SIZE`
- [ ] **6.** One box on the left end of the grass — walking left is stopped by that box
- [ ] **7.** One box on the right end, at `MAX_HORIZONTAL` — walking right is stopped by that box
- [ ] **8.** `while` and `next_y` stack both walls up to the top of the window
- [ ] **9.** `next_platform_y` and an `if`: one platform tile, 2 tiles above the floor
- [ ] **10.** After each platform, `next_platform_y += 2 * TILE_SIZE` — a column of platforms up the window
- [ ] **11.** Each platform is a short row of 3 tiles you can stand on
- [ ] **12.** `random.randint(2, 4)` picks the platform width — restarting changes the width
- [ ] **13.** Tune width: `randint(2, 2)` is always 2 tiles, `randint(2, 4)` varies, then leave `(2, 4)`
- [ ] **14.** Rise uses `random.randint(1, 2)` — platforms step up by 1 or 2 tiles
- [ ] **15.** Tune rise: always `1` is an easy ladder, always `3` is hard to reach, then leave `(1, 2)`
- [ ] **16.** Remember the previous platform’s x so the next one lines up with it
- [ ] **17.** Shift that x by `random.randint(-3, 3)` tiles, keeping the platform between the walls
- [ ] **18.** Your own `build_world_up_to(self, far_y)` — same look, the `while` lives in that method
- [ ] **19.** `self.next_y` remembers how high the walls already go — calling the method again adds tiles above, without a second copy of the floor walls
- [ ] **20.** `arcade.Camera2D` and `.use()` in `on_draw` — the picture looks the same
- [ ] **21.** Camera x sits at `MAX_HORIZONTAL / 2` — the shaft is centered in the window
- [ ] **22.** Camera y is `player.center_y` — at the start the floor sits in the middle of the window
- [ ] **23.** Tune camera y: `max(player.center_y, WINDOW_HEIGHT / 2)` keeps the floor at the bottom until the climb passes the middle
- [ ] **24.** From `on_update`, build up to `player.center_y + 2 * WINDOW_HEIGHT` — jumping keeps revealing new platforms
- [ ] **25.** `arcade.Text` drawn with the world camera — the words scroll away when you jump
- [ ] **26.** A second camera used only for the text — the words stay in the corner while the world scrolls
- [ ] **27.** The text shows tiles climbed; tune `font_size` (12 is small, 36 is large, then leave 18)
- [ ] **28.** Widen `MAX_HORIZONTAL` past the window and clamp camera x so the view never shows past either wall; set the constant back to `10 * TILE_SIZE` and leave a TRY THIS note
