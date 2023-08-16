import numpy as np

class AnteReliability_Rest:
    def __init__(self, observation):
        # Initially, the AnteReliability_Flee is equal to the contextual mapping due to the design of our experiment.
        # Others parameters are initially equal to 0, and we have an observation of our environment which serve as
        # contextual_mapping.
        self.observation = observation
        self.contextual_mapping = self.observation

    def update_contextual(self, biome, mu_rest, learning_rate):
        self.contextual_mapping[biome] = learning_rate * mu_rest + \
                                         (1 - learning_rate) * self.contextual_mapping[biome]
        return self.contextual_mapping

    def update_lambda(self, lambda_rest, biome, tau, mu_rest):
        lambda_rest[biome] = self.contextual_mapping[biome] * np.sum(np.multiply(tau, mu_rest))  # NORMALISE
        return lambda_rest
