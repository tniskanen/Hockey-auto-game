import arcade


class Player(arcade.Sprite):
    def __init__(self, hit, energy, accuracy, name, image):
        self.hit = hit
        self.energy = energy
        self.accuracy = accuracy
        self.name = name
        self.image = image
        super().__init__(self.image, scale=.1)

shop1 = []
for i in range(12):
    ovechkin = Player(hit= 300, 
                    energy= 400, accuracy= 0.33, 
                    name= 'Ovechkin', 
                    image='player_images\ovechkin_player1.png'
                    )

    burns = Player(hit= 600, 
                energy= 350, accuracy= .1, 
                name= 'Burns', 
                image='player_images\\burns_player.png'
                )

    crosby = Player(hit= 250, 
                    energy= 350, accuracy= .1, 
                    name= 'Crosby', 
                    image='player_images\crosby_player.png'
                    )

    shop1.append(ovechkin)
    shop1.append(burns)
    shop1.append(crosby)
