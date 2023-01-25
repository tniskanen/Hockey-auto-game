import arcade
import arcade.gui
import players as p
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'HOCKEY BRAWLERS'

class TeamView(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        self.setup()
        
    def on_draw(self):
        self.clear()

        self.ui_manager.draw()
        self.scoreboard.draw()
        self.score.draw()

        self.current_team.draw()
        self.shop_sprite_list.draw()

    def on_update(self, delta_time: float):
        self.shop_sprite_list.update()
        self.current_team.update()

    def setup(self):
        self.current_team = arcade.SpriteList() 
        self.shop_sprite_list = arcade.SpriteList()

        self.shop_list = []
        self.all_players = []
        self.Crosby = p.Crosby()
        self.Burns = p.Burns()
        self.Ovechkin = p.Ovechkin()

        self.all_players.append(self.Crosby)
        self.all_players.append(self.Burns)
        self.all_players.append(self.Ovechkin)

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

    def create_sprites(self, list):
        length = len(list)
        for i in range(length):
            image = list[i].image
            name = list[i].name
            name = arcade.Sprite(image,
                                 scale=.15
                                         )
            self.shop_sprite_list.append(name)
            #print(self.shop_sprite_list[i])
    def position_sprites(self, SpriteList):
        SpriteList[0].set_position(center_x=SCREEN_WIDTH*.6,
                                   center_y=SCREEN_HEIGHT*.8)
        SpriteList[1].set_position(center_x=SCREEN_WIDTH*.7,
                                   center_y=SCREEN_HEIGHT*.8)
        SpriteList[2].set_position(center_x=SCREEN_WIDTH*.8,
                                   center_y=SCREEN_HEIGHT*.8)
        SpriteList[3].set_position(center_x=SCREEN_WIDTH*.9,
                                   center_y=SCREEN_HEIGHT*.8)

    def refresh_button_clicked(self, event):
        self.shop_sprite_list.clear()
        self.shop_list.clear()
        for i in range(0, 4):
            num = random.randint(0, 2)
            player = self.all_players[num]
            self.shop_list.append(player)
        self.create_sprites(self.shop_list)
        self.position_sprites(self.shop_sprite_list)

    def lock(self, event):
        pass

            
if __name__ == '__main__':
    window = TeamView()
    arcade.run()