from environment import Environment
from agent import Agent


# Create the environment and agent
survival_env = Environment()
bob = Agent(delta=2) # arg = 1,2 or 3 := difficulty

survival_env.choose_biome() # random choice of the biome
survival_env.choose_food() # sample of food giving the environment
survival_env.choose_predation() # random choice of predation level between 0 and 100%
survival_env.multiply_food() # computation of all levels of attributes given food and quantity
survival_env.summary_matrix() # creation of the summary stat matrix

# Get the user's input for aversion to risk
risk_aversion = float(input("Enter your aversion to risk (a number between 0 and 100): "))

# Print the initial state of the environment and agent
print("Current biome: ", survival_env.current_biome['name'])
print("Current food: ")
for food_item in survival_env.current_food:
    print(food_item)
print("Predation level: ", survival_env.predation_level)
matrix2 = survival_env.summary_matrix()
for row in matrix2:
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
