# TODO: create player Sprite, put in a SpriteList, draw it in on_draw
import arcade
import sys
ENV_TAG = ".venv" if sys.prefix != sys.base_prefix else "system Python"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 1600
WINDOW_TITLE = "Platformer"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, f"Platformer ({ENV_TAG})")
        self.background_color = arcade.color.AMAZON
        print("GameWindow created")

    def on_draw(self):
        self.clear()

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
