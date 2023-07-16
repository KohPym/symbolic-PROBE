import random

biome1 = {
    'name': 'Rainforest',
    'humidity': 'wet',
    'temperature': random.randint(23, 30),
    'predation': 'high',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 500),
    'oxygen': 'high',
}

biome2 = {
    'name': 'Desert',
    'humidity': 'dry',
    'temperature': random.randint(25, 45),
    'predation': 'low',
    'vegetation': False,
    'water': False,
    'altitude': random.randint(0, 1000),
    'oxygen': 'normal',
}

biome3 = {
    'name': 'Tundra',
    'humidity': 'dry',
    'temperature': random.randint(-15, -5),
    'predation': 'medium',
    'vegetation': False,
    'water': False,
    'altitude': random.randint(500, 2000),
    'oxygen': 'normal',
}

biome4 = {
    'name': 'Plains',
    'humidity': 'moderate',
    'temperature': random.randint(15, 30),
    'predation': 'high',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 1000),
    'oxygen': 'normal',
}

biome5 = {
    'name': 'Savanna',
    'humidity': 'moderate',
    'temperature': random.randint(20, 35),
    'predation': 'high',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 1000),
    'oxygen': 'normal',
}

biome6 = {
    'name': 'Mangrove',
    'humidity': 'wet',
    'temperature': random.randint(25, 35),
    'predation': 'medium',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 100),
    'oxygen': 'high',
}

biome7 = {
    'name': 'Mountains',
    'humidity': 'moderate',
    'temperature': random.randint(-10, 10),
    'predation': 'high',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(2000, 4000),
    'oxygen': 'high',
}

biome8 = {
    'name': 'Swamp',
    'humidity': 'wet',
    'temperature': random.randint(15, 30),
    'predation': 'medium',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(0, 500),
    'oxygen': 'low',
}

biome9 = {
    'name': 'Taiga',
    'humidity': 'moderate',
    'temperature': random.randint(-10, 10),
    'predation': 'high',
    'vegetation': True,
    'water': True,
    'altitude': random.randint(500, 2000),
    'oxygen': 'normal',
}

biome10 = {
    'name': 'Beach',
    'humidity': 'moderate',
    'temperature': random.randint(20, 35),
    'predation': 'low',
    'vegetation': False,
    'water': True,
    'altitude': random.randint(0, 100),
    'oxygen': 'normal',
}

biome11 = {
    'name': 'Random Biome',
    'humidity': random.choice(['wet', 'moderate', 'dry']),
    'temperature': random.randint(-30, 50),
    'predation': random.choice(['low', 'medium', 'high']),
    'vegetation': random.choice([True, False]),
    'water': random.choice([True, False]),
    'altitude': random.randint(0, 5000),
    'oxygen': random.choice(['low', 'normal', 'high']),
}
