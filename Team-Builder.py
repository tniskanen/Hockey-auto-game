import arcade
import arcade.gui


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'HOCKEY BRAWLERS'

class TeamView(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)

        self.scoreboard = arcade.Text(f'Win/Loss/Draw Ratio',
                                      start_x= SCREEN_WIDTH * .01,
                                      start_y= SCREEN_HEIGHT * .95,
                                      color=(255,255,255),
                                      font_size=14,
                                      )
        
        self.score = arcade.Text(f'10-3-0',
                                      start_x= SCREEN_WIDTH * .05,
                                      start_y= SCREEN_HEIGHT * .9,
                                      color=(255,255,255),
                                      font_size=14,
                                      )        
    
        self.ui_manager = arcade.gui.UIManager() #self.window could be argument

        widgets = arcade.gui.UILayout()

        # Refresh button
        normal_texture = arcade.load_texture('refresh.png')
        hover_texture = arcade.load_texture('refresh_hovered.png')
        press_texture = arcade.load_texture('refresh_pressed.png')

        self.refresh_button = arcade.gui.UITextureButton(
            x = SCREEN_WIDTH * .7,
            y = SCREEN_HEIGHT * .6,
            width= SCREEN_WIDTH * .075,
            height= SCREEN_HEIGHT * .05,            
            texture = normal_texture,
            texture_hovered= hover_texture,
            texture_pressed= press_texture
        )

        self.refresh_button.on_click = self.refresh_button_clicked #function needs to be created

        widgets.add(self.refresh_button)

        # Lock button
        normal_texture = arcade.load_texture('lock.png')
        hover_texture = arcade.load_texture('lock_hovered.png')
        press_texture = arcade.load_texture('lock_pressed.png')

        self.lock_button = arcade.gui.UITextureButton(
            x = SCREEN_WIDTH * .8,
            y = SCREEN_HEIGHT * .6,
            width= SCREEN_WIDTH * .075,
            height= SCREEN_HEIGHT * .05,            
            texture = normal_texture,
            texture_hovered= hover_texture,
            texture_pressed= press_texture
        )

        self.lock_button.on_click = self.lock # function needs to be created

        widgets.add(self.lock_button)


        self.ui_manager.add(widgets)


    def refresh_button_clicked(self):
        pass

    def lock(self):
        pass


    def on_draw(self):
        self.clear()

        self.ui_manager.draw()
        self.scoreboard.draw()
        self.score.draw()

if __name__ == '__main__':
    window = TeamView()
    arcade.run()