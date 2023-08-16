import numpy as np
import copy

# The observation matrix is a matrix showing what the agent could observe before the experiment.
# Ensentially, this means what informations on the context the agent could gather.
# In a non-computationnal world, it would basically means the memory and/or a priori that we have
# on our world and biomes, up to our knowledge (e.g, a desert is not a good place to survive).

class ObservationMatrix:
    def __init__(self):
        self.matrix = np.zeros((10, 7))
        self.norm_matrix = np.zeros((10, 7))

    def update(self, current_biome, predation_level, values):
        num_values = len(values)
        self.matrix[current_biome, :num_values] += values
        self.matrix[current_biome, 5] += predation_level / 100
        self.matrix[current_biome, 6] += 1

    def normalize_matrix(self):
        self.norm_matrix = copy.copy(self.matrix)
        row_sums = np.sum(self.norm_matrix[:, :4], axis=1, keepdims=True)
        for i in range(row_sums.shape[0]):
            if row_sums[i] != 0:
                self.norm_matrix[i, :4] = np.round(self.norm_matrix[i, :4] / row_sums[i], 2)
        non_zero_denominator = self.norm_matrix[:, 6] != 0
        self.norm_matrix[:, 5][non_zero_denominator] /= self.norm_matrix[:, 6][non_zero_denominator]
