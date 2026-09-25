import arcade
import sys
ENV_TAG = ".venv" if sys.prefix != sys.base_prefix else "system Python"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Platformer"
TILE_SIZE = 64

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, f"Platformer ({ENV_TAG})")
        self.set_update_rate(1/60)
        print("GameWindow created")
        self.background_color = arcade.color.AMAZON
        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=0.5,
        )
        self.player.center_x = 100
        self.player.center_y = 228
        self.player_list.append(self.player)

        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        for x in range(0, WINDOW_WIDTH, TILE_SIZE):
            grass = arcade.Sprite(
                ":resources:images/tiles/grassMid.png",
                scale=0.5
            )
            grass.center_x = x+TILE_SIZE / 2
            grass.center_y = TILE_SIZE / 2
            self.wall_list.append(grass)

        BOXES = [(256,96),(400,160),(544,224)]
        for x, y in BOXES:    
            box = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", scale=0.5)
            box.center_x = x
            box.center_y = y
            self.wall_list.append(box)
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            walls=self.wall_list,
            gravity_constant=0.1,
        )

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.wall_list.draw()

    # TODO: gravity_constant 0.3, then 2, then set it back to 1
    
    def on_update(self, delta_time):
        self.physics_engine.update()

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
