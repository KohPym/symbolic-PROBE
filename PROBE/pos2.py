# environment.py

import random
import food

class Environment:
    def __init__(self):
        self.foods = []
        self.satiety = 0
        self.vitamins = 0
        self.hydration = 0
        self.toxicity = 0
        self.predation = 0
        self.temperature = ''
        self.wetness = 0
        
        # Choix aléatoire de 5 aliments dans food.py
        self.foods = random.sample([food.apple, food.salmon, food.mushroom, food.blueberry, food.elderberry, food.potato, food.cactus, food.water, food.coconut_water, food.maple_syrup], 5)
        
        # Calcul des jauges en fonction des aliments sélectionnés
        for food in self.foods:
            self.satiety += food['satiety'] * random.uniform(0.5, 1.5)
            self.vitamins += food['vitamins'] * random.uniform(0.5, 1.5)
            self.hydration += food['hydration'] * random.uniform(0.5, 1.5)
            self.toxicity += food['toxicity'] * random.uniform(0.5, 1.5)
        
        # Définition aléatoire de la température
        self.temperature = random.choice(['hot', 'cold'])
        
        # Définition aléatoire de la mouillure
        self.wetness = random.randint(0, 100)
        
        # Définition aléatoire de la prédation
        self.predation = random.randint(0, 100)
        
    def __str__(self):
        return f'Environment: {len(self.foods)} foods, satiety: {self.satiety}, vitamins: {self.vitamins}, hydration: {self.hydration}, toxicity: {self.toxicity}, predation: {self.predation}, temperature: {self.temperature}, wetness: {self.wetness}'
