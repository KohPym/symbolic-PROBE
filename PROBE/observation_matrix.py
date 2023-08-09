import numpy as np

# The observation matrix is a matrix showing what the agent could observe before the experiment.
# Enssentially, this means what informations on the context the agent could gather.
# In a non-computationnal world, it would basically means the memory and/or a priori that we have
# on our world and biomes, up to our knowledge (e.g, a desert is not a good place to survive).

class ObservationMatrix:
    def __init__(self):
        self.matrix = np.zeros((10, 6))

    def update(self, current_biome, values): #Pense à ajouter que 4 valeurs sur 6
        biome_mapping = {
            "Rainforest": 0,
            "Desert": 1,
            "Tundra": 2,
            "Plains": 3,
            "Savanna": 4,
            "Mangrove": 5,
            "Plains": 6,
            "Swamp": 7,
            "Taiga": 8,
            "Beach": 9,
        }
      
        if current_biome in biome_mapping:
            line = biome_mapping[current_biome]
            num_values = len(values)
            self.matrix[line, :num_values] += values

    def normalize_matrix(self):
        norm_matrix = self.matrix
        matrix_sum = np.sum(norm_matrix)
        if matrix_sum != 0:
            norm_matrix /= matrix_sum


    def normalize_matrix(self):
        # Normalise les 4 premiers termes de chaque ligne de la matrice
        self.matrix[:, :4] /= np.sum(self.matrix[:, :4], axis=1, keepdims=True)
