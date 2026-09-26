import arcade
import sys
ENV_TAG = ".venv" if sys.prefix != sys.base_prefix else "system Python"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Platformer"
TILE_SIZE = 64
PLAYER_SPEED = 5
JUMP_POWER = 20

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, f"Platformer ({ENV_TAG})")
        print("GameWindow created")
        self.set_update_rate(1/60)
        self.left_pressed = False
        self.right_pressed = False
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
            gravity_constant=1,
        )

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.wall_list.draw()

    # TODO: TRY THIS comments above PLAYER_SPEED, JUMP_POWER, and gravity_constant
    def on_key_press(self, key, modifier):
        if key == arcade.key.LEFT:
            self.left_pressed = True
        if key == arcade.key.RIGHT:
            self.right_pressed = True
        if key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = JUMP_POWER

    def on_key_release(self, key, modifier):
        if key == arcade.key.LEFT:
            self.left_pressed = False
        if key == arcade.key.RIGHT:
            self.right_pressed = False
    
    def on_update(self, delta_time):
        if self.right_pressed:
            self.player.change_x = PLAYER_SPEED
        elif self.left_pressed:
            self.player.change_x = -PLAYER_SPEED
        else:
            self.player.change_x = 0
            
        self.physics_engine.update()
        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > WINDOW_WIDTH:
            self.player.right = WINDOW_WIDTH
        

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
