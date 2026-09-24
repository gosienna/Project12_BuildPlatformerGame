# Coordinates and Sprites

- In Arcade, **(0, 0) is the bottom-left** of the window. `y` increases upward.
- A **sprite** is a picture with a position (`center_x`, `center_y`) and optional `scale`.
- A **sprite list** (`arcade.SpriteList`) holds many sprites so you can `draw()` them together.
- Built-in art uses paths like `:resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png`.
- **Tiles:** built-in tile images are 128×128; with `scale=0.5` they draw at **64×64** (`TILE_SIZE`).
- **Ground row:** loop `for x in range(0, WINDOW_WIDTH, TILE_SIZE)` and place one grass tile at each `x`. Put `center_y` at `TILE_SIZE / 2` so the tile sits on the bottom edge.
- Walls that never move can use `arcade.SpriteList(use_spatial_hash=True)` for faster collision later.
