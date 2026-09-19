# TODO: WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE — use them in super().__init__
import arcade

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Platformer")
        print("GameWindow created")

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
