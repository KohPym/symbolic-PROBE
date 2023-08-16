import numpy as np

class AnteReliability_Flee:
    def __init__(self, observation):
        # Initially, the AnteReliability_Flee is equal to the contextual mapping due to the design of our experiment.
        # Others parameters are initially equal to 0, and we have an observation of our environment which serve as
        # contextual_mapping.
        self.observation = observation
        self.contextual_mapping = self.observation

    def update_contextual(self, biome, mu_flee, learning_rate):
        self.contextual_mapping[biome] = learning_rate * mu_flee + \
                                         (1 - learning_rate) * self.contextual_mapping[biome]
        return self.contextual_mapping

    def update_lambda(self, lambda_flee, biome, tau, mu_flee):
        lambda_flee[biome] = self.contextual_mapping[biome] * np.sum(np.multiply(tau, mu_flee))  # NORMALISE
        return lambda_flee

