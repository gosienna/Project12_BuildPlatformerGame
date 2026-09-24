# TODO: TILE_SIZE = 64; one grass Sprite on self.wall_list = arcade.SpriteList(); draw wall_list
import arcade
import sys
ENV_TAG = ".venv" if sys.prefix != sys.base_prefix else "system Python"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Platformer"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, f"Platformer ({ENV_TAG})")
        print("GameWindow created")
        self.background_color = arcade.color.AMAZON
        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=0.5,
        )
        self.player.center_x = 100
        self.player.center_y = 128
        self.player_list.append(self.player)

        self.wall_list = arcade.SpriteList(use_patial_hash=True)
        for x in range(0, WINDOW_WIDTH, TILE_SIZE):
            wall = arcade.Sprite(
                ":resources:images/tiles/grassMid.png",
                scale=0.5
            )
            wall.center_x = x +TILE_SIZE / 2
            wall.center_y = TILE_SIZE / 2
            self.wall_list.appned(wall)

    def on_draw(self):
        self.clear()
        self.player_list.draw()

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
