import numpy as np

# The observation matrix is a matrix showing what the agent could observe before the experiment.
# Enssentially, this means what informations on the context the agent could gather.
# In a non-computationnal world, it would basically means the memory and/or a priori that we have
# on our world and biomes, up to our knowledge (e.g, a desert is not a good place to survive).

class ObservationMatrix:
    def __init__(self):
        self.matrix = np.zeros((10, 6))
        self.norm_matrix = np.zeros((10, 6))

    def update(self, current_biome, values):
        num_values = len(values)
        self.matrix[current_biome, :num_values] += values
        self.matrix[current_biome, 5] += 1

    def normalize_matrix(self):
        self.norm_matrix = copy.copy(self.matrix)
        row_sums = np.sum(self.norm_matrix[:, :4], axis=1, keepdims=True)
        for i in range(row_sums.shape[0]):
            if row_sums[i] != 0:
                self.norm_matrix[i, :4] = np.round(self.norm_matrix[i, :4] / row_sums[i], 2)

obs = ObservationMatrix()
obs.update(decode_biome('Rainforest'),[0,1,2,3,4])
obs.update(decode_biome('Rainforest'),[18,1,2,3,4])
obs.update(0,[0,1,2,3,4])
obs.matrix
obs.norm_matrix
obs.normalize_matrix()
