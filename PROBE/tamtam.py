def count_matching_biomes(humidity, vegetation, water):
    biomes = [biome1, biome2, biome3, biome4, biome5, biome6, biome7, biome8, biome9, biome10]
    counts = {
        'humidity': 0,
        'vegetation': 0,
        'water': 0,
        'humidity_water': 0  # Compte pour l'occurrence simultanée de humidity et water
    }

    for biome in biomes:
        if biome['humidity'] == humidity:
            counts['humidity'] += 1
        if biome['vegetation'] == vegetation:
            counts['vegetation'] += 1
        if biome['water'] == water:
            counts['water'] += 1
        if biome['humidity'] == humidity and biome['water'] == water:
            counts['humidity_water'] += 1

    return counts

# Exemple d'utilisation
humidity_arg = 'wet'
vegetation_arg = True
water_arg = True

matching_counts = count_matching_biomes(humidity_arg, vegetation_arg, water_arg)
print("Comptes des correspondances :")
print("Humidity :", matching_counts['humidity'])
print("Vegetation :", matching_counts['vegetation'])
print("Water :", matching_counts['water'])
print("Humidity + Water :", matching_counts['humidity_water'])
