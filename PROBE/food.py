import random

food1 = {
    'name': 'Apple',
    'type': 'food',
    'satiety': 8,
    'vitamins': 2,
    'hydration': 5,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 1000),
}

food2 = {
    'name': 'Mushroom',
    'type': 'food',
    'satiety': 5,
    'vitamins': 2,
    'hydration': 1,
    'toxicity': 5,
    'humidity': 'wet',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(-1000, 2000),
}

food3 = {
    'name': 'Blueberry',
    'type': 'food',
    'satiety': 4,
    'vitamins': 2,
    'hydration': 6,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 500),
}

food4 = {
    'name': 'Elderberry',
    'type': 'food',
    'satiety': 3,
    'vitamins': 2,
    'hydration': 6,
    'toxicity': 3,
    'humidity': 'moderate',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 500),
}

food5 = {
    'name': 'Potato',
    'type': 'food',
    'satiety': 6,
    'vitamins': 1,
    'hydration': 3,
    'toxicity': 0,
    'humidity': 'moderate',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 300),
}

food6 = {
    'name': 'Salmon',
    'type': 'food',
    'satiety': 7,
    'vitamins': 2,
    'hydration': 2,
    'toxicity': 0,
    'humidity': 'wet',
    'vegetation': False,
    'water': True,
    'altitude': random.randint(-1000, 300),
}

food7 = {
    'name': 'Cactus',
    'type': 'food',
    'satiety': 3,
    'vitamins': 1,
    'hydration': 10,
    'toxicity': 1,
    'humidity': 'dry',
    'vegetation': False,
    'water': False,
    'altitude': random.randint(0, 300),
}

food8 = {
    'name': 'Water',
    'type': 'liquid',
    'satiety': 0,
    'vitamins': 0,
    'hydration': 10,
    'toxicity': 0,
    'humidity': 'wet',
    'vegetation': False,
    'water': True,
    'altitude': random.randint(-2000, 1000),
}

food9 = {
    'name': 'Coconut Water',
    'type': 'liquid',
    'satiety': 1,
    'vitamins': 2,
    'hydration': 9,
    'toxicity': 0,
    'humidity': 'wet',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 1000),
}

food10 = {
    'name': 'Maple Syrup',
    'type': 'liquid',
    'satiety': 1,
    'vitamins': 0,
    'hydration': 5,
    'toxicity': 0,
    'humidity': 'wet',
    'vegetation': False,
    'water': True,
    'altitude': random.randint(0,800)
}

random = {
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
