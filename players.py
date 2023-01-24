
class Player:
    def __init__(self, weight, speed, energy, accuracy, name, image):
        self.weight = weight
        self.speed = speed
        self.energy = energy
        self.accuracy = accuracy
        self.name = name
        self.image = image

class sniper(Player):
    def __init__(self, weight= 150, speed= 2, energy= 400, accuracy= 0.33, name= 'Sniper', image=None):
        Player.__init__(self, weight, speed, energy, accuracy, name, image)
    
    def snipe(self):
        self.accuracy *= 2
        pass
        
class protector(Player):
    def __init__(self, weight= 300, speed= 2, energy= 350, accuracy= .1, name= 'Protector', image=None):
        Player.__init__(self, weight, speed, energy, accuracy, name, image)

    def protect(self):
        #if opposing player knocked out teammate
        self.energy *= 2

if __name__ == '__main__':
    player_sniper = sniper()
    player_protector = protector()
    print(player_sniper.energy)
    print(player_protector.weight)
