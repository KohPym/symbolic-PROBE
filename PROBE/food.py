import random

# This file contains all foods required for the environment, that will be selected randomly for a specific biome. It also include a random food with random attributes.
# Attributes refers to the 'name', 'type', 'satiety', 'vitamins', 'hydration', 'toxicity', 'humidity', 'vegetation', 'water' and 'altitude'.
# The random food can be seen both as an independant food and a prototype, giving the range of the attributes of all others foods.

random_food = {
    'name': 'Random Food',
    'type': random.choice(['liquid', 'food']),
    'satiety': random.randint(0,10),
    'vitamins': random.randint(0,10),
    'hydration': random.randint(0,10),
    'toxicity': random.randint(0,10),
    'humidity': random.choice(['wet', 'moderate', 'dry']),
    'vegetation': random.choice([True, False]),
    'water': random.choice([True, False]),
    'altitude': random.randint(0,5000)
}

food1 = {
    'name': 'Apple',
    'type': 'food',
    'satiety': 4,
    'vitamins': 7,
    'hydration': 2,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 1000),
}

food2 = {
    'name': 'Nut',
    'type': 'food',
    'satiety': 3,
    'vitamins': 9,
    'hydration': 0,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 2000),
}

food3 = {
    'name': 'Insect',
    'type': 'food',
    'satiety': 7,
    'vitamins': 2,
    'hydration': 0,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': False,
    'water': False,
    'altitude': random.randint(0, 1000),
}

food4 = {
    'name': 'Rice',
    'type': 'food',
    'satiety': 9,
    'vitamins': 1,
    'hydration': 2,
    'toxicity': 0,
    'humidity': 'wet',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 500),
}

food5 = {
    'name': 'Date',
    'type': 'food',
    'satiety': 3,
    'vitamins': 1,
    'hydration': 1,
    'toxicity': 0,
    'humidity': 'dry',
    'vegetation': False,
    'water': False,
    'altitude': random.randint(0, 300),
}

food6 = {
    'name': 'Sorghum',
    'type': 'food',
    'satiety': 2,
    'vitamins': 1,
    'hydration': 0,
    'toxicity': 0,
    'humidity': 'dry',
    'vegetation': False,
    'water': False,
    'altitude': random.randint(0, 500),
}

food7 = {
    'name': 'Elderberry',
    'type': 'food',
    'satiety': 1,
    'vitamins': 1,
    'hydration': 1,
    'toxicity': 8,
    'humidity': 'wet',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 300),
}

food8 = {
    'name': 'Mushroom',
    'type': 'food',
    'satiety': 1,
    'vitamins': 1,
    'hydration': 0,
    'toxicity': 8,
    'humidity': 'wet',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(-2000, 1000),
}

food9 = {
    'name': 'Salmon',
    'type': 'food',
    'satiety': 2,
    'vitamins': 2,
    'hydration': 8,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(-500, 1000),
}

food10 = {
    'name': 'Water',
    'type': 'liquid',
    'satiety': 0,
    'vitamins': 0,
    'hydration': 10,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': False,
    'water': True,
    'altitude': random.randint(-2000, 1000),
}
