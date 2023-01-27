import arcade 
import start

window = arcade.Window(title='Hockey Brawlers')
window.show_view(start.Start(window))
arcade.run()

