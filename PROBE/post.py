class Food:
    def __init__(self,*args):
        self.args = args

class Apple(Food):
    def __init__(self):
        super().__init__("Apple", 10, 5, 0)

class Cactus(Food):
    def __init__(self):
        super().__init__("Cactus", 2, 8, 2)
