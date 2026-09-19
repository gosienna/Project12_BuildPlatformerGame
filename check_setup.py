# TODO: import sys and arcade
# TODO: print Python and Arcade versions
# TODO: class SetupWindow(arcade.Window) with green background + "Setup OK!" text
# TODO: create SetupWindow() and call arcade.run()
import sys
import arcade

print("Python :", sys.version.split()[0])
print("Arcade :", arcade.__version__)

class SetupWindow(arcade.Window):
    def __init__(self):
        super().__init__(480, 200, "Setup check")
        self.text = arcade.Text("Setup OK! Close this window.", 40, 90, arcade.color.WHITE, 18)
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        self.clear()
        self.text.draw()

SetupWindow()
arcade.run()