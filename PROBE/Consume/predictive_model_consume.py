class PostReliability_Consume:
    def __init__(self, observation):
        # Initially, the AnteReliability_Flee is equal to the contextual mapping due to the design of our experiment.
        # Others parameters are intially equal to 0 and we have an observation of our environment which serve as contextual_mapping.
        # We then apply a decision structure to introduce the interoception mechanism.
        self.observation = observation  # Somme et moeynne pour conso etc
        self.predictive_mapping = self.observation

    def update_predictive(self, biome, lambda_consume, learning_rate):  # Update du contexte F
        self.predictive_mapping[biome] = learning_rate * mu + (1 - learning_rate) * self.predictive_mapping[biome] # Voué a converger
        return self.predictive_mapping

    def update_mu(self, lambda_consume, biome, mu_consume):
        mu_consume[biome] = self.predictive_mapping[biome] * lambda_consume  # NORMALISE
        return mu_consume
