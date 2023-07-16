# C'est bob !

class Agent:
    def __init__(self, delta=2):
        self.health = 50
        self.energy = 80
        self.toxicity = 0
        self.satiety = 80
        self.hydration = 80
        self.delta = delta

    def update(self):
        self.energy -= self.delta / 2
        self.satiety -= self.delta / 2
        self.hydration -= self.delta / 2
        self.toxicity -= 1
        self.toxicity = max(0, self.toxicity)

        self.health -= self.toxicity / 10

        self.health = max(0, self.health)
        self.energy = max(0, self.energy)
        self.satiety = max(0, self.satiety)
        self.hydration = max(0, self.hydration)

    def modify_energy(self, value):
        self.energy += value

    def modify_satiety(self, value):
        self.satiety += value

    def modify_toxicity(self, value):
        self.toxicity += value

    def modify_hydration(self, value):
        self.hydration += value

    def set_delta(self, delta):
        self.delta = delta
