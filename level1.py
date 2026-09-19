# TODO: in __init__, set self.background_color (e.g. arcade.color.AMAZON)
import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 1600
WINDOW_TITLE = "Platformer"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        print("GameWindow created")

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
