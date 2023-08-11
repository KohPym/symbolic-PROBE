# It's bob ! 
 
class Agent:
    def __init__(self, delta=2, health=50, energy=80, satiety=80, hydration=80, toxicity=0):
        """
        Initialize main attributes of the agent. Set the difficulty for the agent to survive in the environment, using the delta parameter.
        This parameter do have an impact on natural decrease of energy, satiety and hydration of the agent.

        Args:
            delta (int) -- Difficulty of the environment, between 1 and 3 (included), default value is 2.
            health (int) -- Health of the agent. If health reach 0, the game is over (On a "Game Over" Mario's Theme). 
            It can oscillate between 0 and 100, default value is 50.
            energy (int) -- Energy of the agent. It can be modified by the vitamin's level of food from the environment. If it reach 0, the agent is forced to rest. Value between 0 and 100, default value is 80.
            satiety (int) -- Satiety of the agent. It is changed by the food's satiety that is consumed by the agent. If it reach 0, the agent lose 1 additionnal health per time unit. Value between 0 and 100, default to 80.
            hydration (int) -- Hydration of the agent. It is changed by the food's hydration. If it reach 0, the agent lose 3 additionnal health per time unit. Value between 0 and 100, default to 80.
            toxicity (int) -- Toxicity of the agent. It can be modified by the food's toxicity. It decrease proportionnaly the health of the agent. Value between 0 and 100, default to 0.
        """
        self.delta = delta
        self.health = health
        self.energy = energy
        self.satiety = satiety
        self.hydration = hydration
        self.toxicity = toxicity

    def update(self):
        """
        Update the agent's level of attributes such as energy and satiety. This method only apply the natural decrease such as losing energy as time passes.
        The natural decrease, at each time point, is equal to 1 (for delta = 2, the default value).
        """
        self.health -= self.toxicity / 10
        self.energy -= self.delta / 2
        self.satiety -= self.delta / 2
        if self.satiety <= 0:
            self.health -= 1
        self.hydration -= self.delta / 2
        if self.hydration <= 0:
            self.health -= 3
        self.toxicity -= 1
     
        self.health = max(0, min(100, self.health))
        self.energy = max(0, min(100, self.energy))
        self.satiety = max(0, min(100, self.satiety))
        self.hydration = max(0, min(100, self.hydration))
        self.toxicity = max(0, min(100, self.toxicity))
     
     # Below a simplified version (but harder to read and less flexible)
     # self.health = max(0, min(100, self.health - self.toxicity / 10))
     # self.energy = max(0, min(100, self.energy - self.delta / 2))
     # self.satiety = max(0, min(100, self.satiety - self.delta / 2))
     # self.hydration = max(0, min(100, self.hydration - self.delta / 2))
     # self.toxicity = max(0, min(100, self.toxicity - 1))

    def modify_delta(self, delta):
        """
        Modifies the difficulty for the agent to survive in the environment. This allow to modify the impact on the environment without changing it.

        Args:
            delta (int) -- The difficulty if the agent to survive in the enrivonment, between 1 and 3 (included).
        """
        self.delta = delta
     
    def modify_health(self, value):
        """
        Modifies the agent's health level.

        Args:
            value (int) -- Amount of health to add on the current value on the agent, can be negative.
        """
        self.health += value
 
    def modify_energy(self, value):
        """
        Modifies the agent's energy level.

        Args:
            value (int) -- Amount of energy to add on the current value on the agent, can be negative.
        """
        self.energy += value

    def modify_satiety(self, value):
        """
        Modifies the agent's satiety level.

        Args:
           value (int) -- Amount of satiety to add on the current value on the agent, can be negative.
        """
        self.satiety += value

    def modify_hydration(self, value):
        """
        Modifies the agent's hydration level.

        Args:
            value (int) -- Amount of hydration to add on the current value on the agent, can be negative.
        """
        self.hydration += value
     
    def modify_toxicity(self, value):
        """
        Modifies the agent's toxicity level.

        Args:
            value (int) -- Amount of toxicity to add on the current value on the agent.
        """
        self.toxicity += value

# Note that we could use a global method for modifying the agent's attributes [modify(0,1,0,5,0) for example] but for the sake of readability, I have opted for independent parts.
