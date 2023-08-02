def decode(arg):
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
