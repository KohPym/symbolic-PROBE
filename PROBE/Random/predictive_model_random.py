class PostReliability_Random:
    def __init__(self, observation):
        self.observation = observation
        self.predictive_mapping = self.observation

    def update_predictive(self, biome, homeostasis_score, action_probability, t):
        self.predictive_mapping[biome] = (homeostasis_score[t] / homeostasis_score[t-1]) * action_probability
        return self.predictive_mapping

    def update_mu(self, lambda_random, biome, mu_random):
        mu_random[biome] = self.predictive_mapping[biome] * lambda_random
        return mu_random
