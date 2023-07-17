from environment import Environment
from agent import Agent

# Create the environment and agent
env = Environment()
agent = Agent()

# Print the initial state of the environment and agent
print("Current biome: ", env.current_biome)
print("Current food: ")
for food_item in env.current_food:
    print(food_item)
print("Predation level: ", env.predation_level)
matrix = env.create_matrix()
for row in matrix:
    print(row)

print("Agent health:", agent.health)
print("Agent energy:", agent.energy)
print("Agent toxicity:", agent.toxicity)
print("Agent satiety:", agent.satiety)
print("Agent hydration:", agent.hydration)

# Modify the agent's attributes
agent.modify_energy(-10)
agent.modify_satiety(-20)
agent.modify_toxicity(30)
agent.modify_hydration(10)

# Update the agent's attributes
agent.update()

# Print the updated state of the agent
print("Agent health:", agent.health)
print("Agent energy:", agent.energy)
print("Agent toxicity:", agent.toxicity)
print("Agent satiety:", agent.satiety)
print("Agent hydration:", agent.hydration)
