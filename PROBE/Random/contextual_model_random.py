import numpy as np

class AnteReliability_Random:
    def __init__(self, observation):
        # Initially, the AnteReliability_Random is equal to the contextual mapping due to the design of our
        # experiment. Others parameters are initially equal to 0, and we have an observation of our environment which
        # serve as contextual_mapping.
        self.observation = observation
        self.contextual_mapping = self.observation

    def update_contextual(self, biome, mu_random, learning_rate):
        self.contextual_mapping[biome] = learning_rate * mu_random + \
                                         (1 - learning_rate) * self.contextual_mapping[biome]
        return self.contextual_mapping

    def update_lambda(self, lambda_random, biome, tau, mu_random):
        lambda_random[biome] = self.contextual_mapping[biome] * np.sum(np.multiply(tau, mu_random))
        return lambda_random
