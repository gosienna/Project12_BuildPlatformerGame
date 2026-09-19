# Arcade Window Basics

Arcade runs a **game loop**: each frame it calls `on_update` (move things) then `on_draw` (paint the screen).

## Minimum window

```python
import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "My Game"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.background_color = arcade.color.AMAZON  # or (r, g, b)

    def on_draw(self):
        self.clear()  # fills with background_color

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
```

## Install (once)

```bash
pip install arcade
```

Then run: `python level1.py`

## Notes

- Subclass `arcade.Window` so you own `__init__`, `on_draw`, and later `on_update` / keyboard handlers.
- `self.clear()` must run at the start of every `on_draw`, or you will see trails / garbage.
- Colors: named constants like `arcade.color.AMAZON`, or an RGB tuple `(0, 100, 50)`.
