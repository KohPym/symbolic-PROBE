from typing import List
from .. import biomes

# tau est obtenu (arg from transition matrix)
# mu a posteriori (arg from different predictive models)
# t-1 est l'unité de temps (arg from main file, int)
# Z normalise
# i = 2 (Flee)
# j = indice sur lequel itérer



energy # from observation_matrix
satiety # from observation_matrix
hydration # from observation_matrix
toxicity # from observation_matrix
risk_aversion # from main loop
predation # from observation_matrix
decoder.decode_biome(arg1) # From main loop

class AnteReliability_Flee:
    def __init__(self, observation):
        # Initially, the AnteReliability_Flee is equal to the contextual mapping due to the design of our experiment.
        # Others parameters are intially equal to 0 and we have an observation of our environment which serve as contextual_mapping.
        # We then apply a decision structure to introduce the interoception mechanism.
        self.observation = observation  # Somme et moeynne pour conso etc
        self.contextual_mapping = self.observation

    def update_contextual(self, biome, mu, learning_rate):  # Update du contexte F
        self.contextual_mapping[biome] = learning_rate * mu + (1 - learning_rate) * self.contextual_mapping[biome] # Voué a converger
        return self.contextual_mapping

    def update_lambda(self, lambda_flee, biome, tau, mu):
        lambda_flee[biome] = self.contextual_mapping[biome] * np.sum(np.multiply(tau, mu))  # NORMALISE
        return lambda_flee


ante = AnteReliability_Flee([1,2,3,4,5,6,7,8,9,10])
ante.update_contextual(7, 1, 0.01)
ante.update_lambda([1,1,1,1,1,1,1,1,1,1], 6, [1,2,3], [2,3,4])

class AnteReliability_Flee:
    def __init__(self, observation):
        # Initially, the AnteReliability_Flee is equal to the contextual mapping due to the design of our experiment.
        # Others parameters are intially equal to 0 and we have an observation of our environment which serve as contextual_mapping.
        # We then apply a decision structure to introduce the interoception mechanism.
        self.observation = observation # Somme et moeynne pour conso etc
        self.contextual_mapping = self.observation

    def decision_structure(self, agent_energy, env_vitamins, agent_satiety, env_satiety, agent_hydration, env_hydration, agent_toxicity, env_toxicity, risk_aversion, env_predation):
        predation_aversion = (70 * (2 - risk_aversion/100)) / 1.4
        if env_predation > predation_aversion:
            return predation_aversion
        else:
            return env_predation
        
    def update_contextual(self, biome, mu, learning_rate): # Update du contexte F
        self.contextual_mapping[biome] = learning_rate * mu + (1 - learning_rate) * self.contextual_mapping[biome]
        self.contextual_list = np.append(self.contextual_list, contextual_mapping)
        return self.contextual_mapping

    def update_lambda(self, lambda_flee, biome, tau, mu):
        lambda_flee[biome] = self.contextual_mapping[biome] * np.multiply([tau, mu]) # NORMALISE
        return lambda_flee

