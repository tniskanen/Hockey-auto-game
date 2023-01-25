
class Player:
    def __init__(self, weight, speed, energy, accuracy, name, image):
        self.weight = weight
        self.speed = speed
        self.energy = energy
        self.accuracy = accuracy
        self.name = name
        self.image = image

class Ovechkin(Player):
    def __init__(self, weight= 150, speed= 2, energy= 400, accuracy= 0.33, name= 'Ovechkin', image='player_images\ovechkin_player1.png'):
        Player.__init__(self, weight, speed, energy, accuracy, name, image)
    
    def ability(self):
        self.accuracy *= 2
        pass
        
class Burns(Player):
    def __init__(self, weight= 300, speed= 2, energy= 350, accuracy= .1, name= 'Burns', image='player_images\\burns_player.png'):
        Player.__init__(self, weight, speed, energy, accuracy, name, image)

    def ability(self):
        #if opposing player knocked out teammate
        self.energy *= 2

class Crosby(Player):
    def __init__(self, weight= 300, speed= 2, energy= 350, accuracy= .1, name= 'Crosby', image='player_images\crosby_player.png'):
        Player.__init__(self, weight, speed, energy, accuracy, name, image)

    def ability(self):
        self.energy += 100



if __name__ == '__main__':
    player_sniper = sniper()
    player_protector = protector()
    print(player_sniper.energy)
    print(player_protector.weight)
