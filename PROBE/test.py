env = Environment()
env.choose_biome()
env.choose_food()
env.multiply_food()
matrix = env.create_matrix()

print("Current biome: ", env.current_biome)

print("Current food: ")
for food_item in env.current_food:
    print(food_item)

for row in matrix:
    print(row)
