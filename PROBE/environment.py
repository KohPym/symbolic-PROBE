import random
import food
import biomes

class Environment:
    def __init__(self):
        """
        Initialization of biomes and food variables (from food.py and biomes.py)
        """
        self.biomes = [biomes.biome1, biomes.biome2, biomes.biome3, biomes.biome4, biomes.biome5, biomes.biome6,
                       biomes.biome7, biomes.biome8, biomes.biome9, biomes.biome10, biomes.random_biome]
        self.current_biome = None
        self.current_food = []
        self.predation_level = None

    def choose_biome(self):
        """
        Random choice of biome.
        """
        self.current_biome = random.choice(self.biomes)

    def compare_attributes(self, food_item):
        """
        Comparison between the attributes of the selected biome and the food available in order to match both of the generation.
        (Meaning that we will not find any cactus in toundra ...)

        Args:
            food_item (str) -- Food to compare with the biome..
        """
        attributes_to_compare = ["humidity", "vegetation", "water"] # Can be modified but must be attributes shared between food and biome
        for attribute in attributes_to_compare:
            if attribute in self.current_biome and attribute in food_item and self.current_biome[attribute] != food_item[attribute]:
                return False
        return True

    def choose_food(self):
        """
        Choose food to build the environment based on all food existing in food.py and the matching attributes between the selected biomes and potential food.
        """
        self.current_food = []
        for food_item in [food.food1, food.food2, food.food3, food.food4, food.food5, food.food6,
                          food.food7, food.food8, food.food9, food.food10]:                              
                              # food.random is not yet added but exist inside the food.py file                             
            if self.compare_attributes(food_item):
                self.current_food.append(food_item)
        # Below a list comprehension of the previous loop, avoided to insure a better portability and readibility of the code.
        # self.current_food = [food_item for food_item in [food.food1, food.food2, food.food3, food.food4, food.food5, food.food6, food.food7, food.food8, food.food9, food.food10] if self.compare_attributes(food_item)]
                
    def choose_predation(self):
        """
        Initilization of the predation's level (percentage) to determine the dangerosity (animal) of the environment. Value between 0 and 100. 0 meaning no risk.
        """
        self.predation_level = random.randint(0, 100)

    def multiply_food(self):
        """
        Initilization food's quantity variables of the environment and thus, the level of satiety, hydration, toxicity and vitamins associated to the food (and the environment).
        """
        for food_item in self.current_food:
            food_item['quantity'] = random.randint(1, 5)
            food_item['satiety'] = food_item['satiety'] * food_item['quantity']
            food_item['hydration'] = food_item['hydration'] * food_item['quantity']
            food_item['toxicity'] = food_item['toxicity'] * food_item['quantity']
            food_item['vitamins'] = food_item['vitamins'] * food_item['quantity']

    def summary_matrix(self):
        """
        Matrix summarizing the whole level of satiety, hydration, vitamins, toxicity and quantity of the current environment. This will help to see clearly the evolution of the environment.
        """
        matrix = []
        headers = ["Satiety", "Hydration", "Vitamins", "Toxicity", "Quantity"]
        for food_item in self.current_food:
            matrix.append([
                food_item['satiety'],
                food_item['hydration'],
                food_item['vitamins'],
                food_item['toxicity'],
                food_item['quantity']
            ])
        total_row = [sum(col) for col in zip(*matrix)]
        matrix.append(total_row)
        matrix.insert(0, headers)
        return matrix
