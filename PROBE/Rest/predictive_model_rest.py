class PostReliability_Rest:
    def __init__(self, observation):
        self.observation = observation
        self.predictive_mapping = self.observation

    def update_predictive(self, biome, homeostasis_score, action_probability, t):
        self.predictive_mapping[biome] = (homeostasis_score[t] / homeostasis_score[t-1]) * action_probability
        return self.predictive_mapping

    def update_mu(self, lambda_rest, biome, mu_rest):
        mu_rest[biome] = self.predictive_mapping[biome] * lambda_rest
        return mu_rest
