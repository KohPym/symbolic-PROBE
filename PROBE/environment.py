import random
import food
import biomes

class Environment:
    def __init__(self):
        self.biomes = [biomes.biome1, biomes.biome2, biomes.biome3, biomes.biome4, biomes.biome5, biomes.biome6,
                       biomes.biome7, biomes.biome8, biomes.biome9, biomes.biome10, biomes.biome11]
        self.current_biome = None
        self.current_food = []

    def choose_biome(self):
        self.current_biome = random.choice(self.biomes)

    def compare_attributes(self, food_item):
        attributes_to_compare = ["humidity", "vegetation", "water"]
        for attribute in attributes_to_compare:
            if attribute in self.current_biome and attribute in food_item and self.current_biome[attribute] != food_item[attribute]:
                return False
        return True

    def choose_food(self):
        self.current_food = []
        for food_item in [food.apple, food.mushroom, food.blueberry, food.elderberry, food.potato, food.salmon,
                          food.cactus, food.water, food.coconut_water, food.maple_syrup]:
            if self.compare_attributes(food_item):
                self.current_food.append(food_item)

    def multiply_food(self):
        for food_item in self.current_food:
            food_item['quantity'] = random.randint(1, 5)
            food_item['satiety'] = food_item['satiety'] * food_item['quantity']
            food_item['hydration'] = food_item['hydration'] * food_item['quantity']
            food_item['toxicity'] = food_item['toxicity'] * food_item['quantity']
            food_item['vitamins'] = food_item['vitamins'] * food_item['quantity']

    def create_matrix(self):
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
