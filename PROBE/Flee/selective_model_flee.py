models = [model = SymbolicQLearning(env, env.dist) for _ in range(8)]

models[i].learn(...)

total_timesteps=10000, learning_rate=0.1, discount_factor=0.5, radius=0.001, log_name=f"runs/symbolic-ql-{r}"

env1 = SymbolicEnv("folder/o1.yaml", "folder/i1.yaml")
env2 = SymbolicEnv("folder/o2.yaml", "folder/i2.yaml")
...

np.argmax(model.qtable[tuple(observation)])
