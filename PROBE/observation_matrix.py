import numpy as np

class ObservationMatrix:
    def __init__(self):
        self.matrix = np.zeros((10, 5))

    def update(self, current_biome, values):
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
            self.matrix[line] += values

    def normalize_matrix(self):
        norm_matrix = self.matrix
        matrix_sum = np.sum(norm_matrix)
        if matrix_sum != 0:
            norm_matrix /= matrix_sum
