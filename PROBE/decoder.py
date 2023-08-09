def decode_task_set(arg):
    if isinstance(arg, str):
        mapping = {
            "Consume": 1,
            "Flee": 2,
            "Random": 3,
            "Rest": 4,
            "Stock": 5
        }
        return mapping.get(arg, "Invalid input: string not recognized")
    elif isinstance(arg, int):
        mapping = {
            1: "Consume",
            2: "Flee",
            3: "Random",
            4: "Rest",
            5: "Stock"
        }
        return mapping.get(arg, "Invalid input: integer not recognized")
    else:
        return "Invalid input: argument must be a string or an integer"

def decode_biome(arg):
    if isinstance(arg, str):
        biome_mapping = {
            "Rainforest": 0,
            "Desert": 1,
            "Tundra": 2,
            "Plains": 3,
            "Savanna": 4,
            "Mangrove": 5,
            "Plains": 6,
            "Swamp": 7,
            "Taiga": 8,
            "Beach": 9
        }
        return biome_mapping.get(arg, "Invalid input: string not recognized")
    elif isinstance(arg, int):
        biome_mapping = {
            0: "Rainforest",
            1: "Desert",
            2: "Tundra",
            3: "Plains",
            4: "Savanna",
            5: "Mangrove",
            6: "Plains",
            7: "Swamp",
            8: "Taiga",
            9: "Beach"
        }
        return biome_mapping.get(arg, "Invalid input: integer not recognized")
    else:
        return "Invalid input: argument must be a string or an integer"
