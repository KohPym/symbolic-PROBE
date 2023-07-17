from typing import List
from .. import biomes

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
