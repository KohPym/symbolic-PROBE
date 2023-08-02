class Decoder:
    def __init__(self):
        self.mapping_str_to_int = {
            "Consume": 1,
            "Flee": 2,
            "Random": 3,
            "Rest": 4,
            "Stock": 5
        }
        self.mapping_int_to_str = {
            1: "Consume",
            2: "Flee",
            3: "Random",
            4: "Rest",
            5: "Stock"
        }

    def decode(self, arg):
        if isinstance(arg, str):
            return self.mapping_str_to_int.get(arg, "Invalid input: string not recognized")
        elif isinstance(arg, int):
            return self.mapping_int_to_str.get(arg, "Invalid input: integer not recognized")
        else:
            return "Invalid input: argument must be a string or an integer"
