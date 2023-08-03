from typing import List
from .. import biomes

# tau est obtenu (arg from transition matrix)
# mu a posteriori (arg from different predictive models)
# t-1 est l'unité de temps (arg from main file, int)
# Z normalise

class AnteReliability_Flee:
    def __init__(self, mu, tau, t):
        self.mu = mu
        self.tau = tau
        self.t = t
    
    def contextual_mapping(self, x1, x2):
        # On calcule le produit scalaire entre x1 et x2
        dot_product = sum([x1[i] * x2[i] for i in range(len(x1))])
        # On calcule la norme de x1 et x2
        norm_1 = sum([x1[i] ** 2 for i in range(len(x1))]) ** 0.5
        norm_2 = sum([x2[i] ** 2 for i in range(len(x2))]) ** 0.5
        # On calcule le cosinus de l'angle entre x1 et x2
        cos_angle = dot_product / (norm_1 * norm_2)
        # On calcule le ContextualMapping
        return (cos_angle + 1) / 2
    
    def ex_ante_reliability(self):
        # On calcule la somme des produits entre les éléments de tau et de mu
        product_sum = 1
        for i in range(len(self.tau)):
            product_sum *= self.tau[i] * self.mu[i] #Un sum serait plus approprié (A CHANGER)
        
        # On calcule le terme de normalisation
        norm_term = 0
        for i in range(len(self.tau)):
            for j in range(len(self.mu)):
                norm_term += self.contextual_mapping(self.tau[i], self.mu[j])
        norm_term *= len(self.tau) * len(self.mu)
        
        # On calcule la ExAnteReliability
        return product_sum * self.contextual_mapping(self.tau[self.t], self.mu[self.t]) / norm_term

import random

class AnteReliability_Flee:
    def __init__(self, tau=1, mu=1, time=1):
        self.tau = tau
        self.mu = mu
        self.time = time
        
    def run_simulation(self):
        reliability = 1.0
        time_elapsed = 0
        
        while time_elapsed < self.time:
            # On simule une défaillance avec une probabilité mu
            if random.random() < self.mu:
                reliability *= 0.5
            
            # On simule une réparation avec une probabilité tau
            if random.random() < self.tau:
                reliability = min(1.0, reliability * 2.0)
            
            time_elapsed += 1
        
        return reliability

class ContextualModelFlee:
    def __init__(self):
        self.tau = None
        self.mu = None
        self.lambdas = None
    
    def init_lambdas(self):
        self.lambdas = {biome: [0.25] * len(self.mu) for biome in BIOMES}
    
    def set_tau(self, tau_ij):
        self.tau = tau_ij
    
    def set_mu(self, mu_j):
        self.mu = mu_j
        self.init_lambdas()

    def calculate_norm_term(self):
        norm_term = 0
        for biome in BIOMES:
            for j in range(len(self.mu)):
                norm_term += self.tau[biome][j] * self.mu[j]
        return norm_term

    def update_lambdas(self, flee_score):
        norm_term = self.calculate_norm_term()
        for biome in BIOMES:
            for j in range(len(self.mu)):
                lambda_ij = self.lambdas[biome][j] * self.tau[biome][j] * self.mu[j]
                lambda_ij *= flee_score / norm_term
                self.lambdas[biome][j] = lambda_ij

    def get_lambdas(self):
        return [self.lambdas[biome] for biome in BIOMES]

class ContextualModelFlee:
    def __init__(self):
        self.tau = 0.25
        self.N = 4
        self.lambdas = {biome: [0.25]*self.N for biome in BIOMES}

    def generate_lambdas(self, previous_action: str, mus: List[float]) -> List[List[float]]:
        tau_ij = 1 - self.tau if previous_action == 'Flee' else 1/self.N - 1
        norm_term = sum([tau_ij * mu_j for mu_j in mus])

        for biome in BIOMES:
            lambdas_i = []
            for j in range(self.N):
                lambda_ij = self.lambdas[biome][j] * tau_ij * mus[j] / norm_term
                lambdas_i.append(lambda_ij)
            self.lambdas[biome] = lambdas_i

        return [self.lambdas[biome] for biome in BIOMES]


def flee_score(risk_aversion, predation_level):
    score = max(0, min(((1+(risk_aversion/200)) * predation_level), 100))
    return score

add toxicity
