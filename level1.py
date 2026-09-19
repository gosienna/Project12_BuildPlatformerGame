# TODO: import sys; ENV_TAG; use f"Platformer ({ENV_TAG})" in super().__init__
import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 1600
WINDOW_TITLE = "Platformer"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.background_color = arcade.color.AMAZON
        print("GameWindow created")

    def on_draw(self):
        self.clear()

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
