"""
Example code showing how to create a button,
and the three ways to process button events.
"""
import arcade
import arcade.gui
import TeamBuilder


# --- Method 1 for handling click events,
# Create a child class.
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class Start(arcade.View):
    def __init__(self, window: arcade.Window):
        super().__init__(window)

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        

        # Set background color

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        # settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        # self.v_box.add(settings_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        # @settings_button.event("on_click")
        # def on_click_settings(event):
        #     print("Settings:", event)

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_start(self, event):
        print("I'm worthless")

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

if __name__ == '__main__':
    window = arcade.Window
    window.show_view(Start(window))
    arcade.run()
