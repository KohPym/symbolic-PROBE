from SymbolicEnv import SymbolicEnv

class SelectiveModel_Rest:
    def __init__(self):
        self.env = SymbolicEnv()
        check_env(env)

    def train_qlearning(self, total_timesteps, learning_rate, discount_factor, log_name="runs/ql"):
        model = QLearning(self.env)
        model.learn(total_timesteps, learning_rate, discount_factor, log_name)

    def train_symbolic_qlearning(self, total_timesteps, learning_rate, discount_factor, radius, log_name=f"runs/symbolic-ql-{r}"):
        radii = np.linspace(0.01, 0.25, 10)
        for r in radii:
            model = SymbolicQLearning(self.env, self.env.dist)
            model.learn(total_timesteps, learning_rate, discount_factor, radius, log_name)
          
    def action_to_choose(self):
      return np.argmax(model.qtable[tuple(observation)])
