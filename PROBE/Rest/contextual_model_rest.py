class AnteReliability_Rest:
    def __init__(self, observation):
        # Initially, the AnteReliability_Flee is equal to the contextual mapping due to the design of our experiment.
        # Others parameters are intially equal to 0 and we have an observation of our environment which serve as contextual_mapping.
        # We then apply a decision structure to introduce the interoception mechanism.
        self.observation = observation  # Somme et moeynne pour conso etc
        self.contextual_mapping = self.observation

    def update_contextual(self, biome, mu, learning_rate):  # Update du contexte F
        self.contextual_mapping[biome] = learning_rate * mu + (1 - learning_rate) * self.contextual_mapping[biome] # Voué a converger
        return self.contextual_mapping

    def update_lambda(self, lambda_rest, biome, tau, mu):
        lambda_rest[biome] = self.contextual_mapping[biome] * np.sum(np.multiply(tau, mu))  # NORMALISE
        return lambda_rest
