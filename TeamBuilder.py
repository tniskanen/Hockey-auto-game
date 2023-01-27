import arcade
import arcade.gui
from players import shop1
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'HOCKEY BRAWLERS'

class TeamBuilder(arcade.View):
    def __init__(self):
        super().__init__()

        self.setup()
        
    def on_draw(self):
        self.clear()

        self.ui_manager.draw()
        self.scoreboard.draw()
        self.score.draw()

        self.current_team.draw()
        self.shop_sprite_1.draw()
        self.shop_sprite_2.draw()
        self.shop_sprite_3.draw()
        self.shop_sprite_4.draw()

    # def on_update(self, delta_time: float):
    #     self.shop_list.update()
    #     self.current_team.update()

    def setup(self):
        self.current_team = arcade.SpriteList()


        self.refresh_button_clicked(event=True)

        # widget buttons
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

        #activates widgets
        self.ui_manager.enable() 

        self.widgets = arcade.gui.UILayout()

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

        self.widgets.add(self.refresh_button)

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

        self.widgets.add(self.lock_button)


        self.ui_manager.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.widgets))
        

    def position_shop_sprites(self, list1, list2, list3, list4):
        list1.set_position(center_x=SCREEN_WIDTH*.6,
                                    center_y=SCREEN_HEIGHT*.8)
        list2.set_position(center_x=SCREEN_WIDTH*.7,
                                   center_y=SCREEN_HEIGHT*.8)
        list3.set_position(center_x=SCREEN_WIDTH*.8,
                                   center_y=SCREEN_HEIGHT*.8)
        list4.set_position(center_x=SCREEN_WIDTH*.9,
                                   center_y=SCREEN_HEIGHT*.8)

    def refresh_button_clicked(self, event):
        high = len(shop1) 
        quarter = high/4
        half = high/2
        quarter3 = high/4 *3
        self.shop_sprite_1 = shop1[random.randint(0, quarter)]
        self.shop_sprite_2 = shop1[random.randint(quarter+1, half)]
        self.shop_sprite_3 = shop1[random.randint(half+1, quarter3)]
        self.shop_sprite_4 = shop1[random.randint(quarter3+1, high-1)]
        
        self.position_shop_sprites(self.shop_sprite_1, self.shop_sprite_2,
                                   self.shop_sprite_3, self.shop_sprite_4)
            

    def lock(self, event):
        pass

    
    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        #activates widgets
        self.ui_manager.enable()

    def on_hide_view(self):
        self.ui_manager.disable()

            
if __name__ == '__main__':
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    team_builder = TeamBuilder()
    window.show_view(team_builder)
    team_builder.setup()
    arcade.run()