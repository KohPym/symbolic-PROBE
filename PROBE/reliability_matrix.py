import numpy as np


class AnteReliability:
    def __init__(self, ContextualMapping_Consume, ContextualMapping_Flee, ContextualMapping_Random,
                 ContextualMapping_Rest, duration):
        self.n_matrix = None
        self.duration = duration
        self.ContextualMapping_Consume = ContextualMapping_Consume
        self.ContextualMapping_Flee = ContextualMapping_Flee
        self.ContextualMapping_Random = ContextualMapping_Random
        self.ContextualMapping_Rest = ContextualMapping_Rest

        # Création des matrices de 1 colonne et 10 lignes
        self.matrix_consume = np.zeros((10, self.duration))
        self.matrix_flee = np.zeros((10, self.duration))
        self.matrix_random = np.zeros((10, self.duration))
        self.matrix_rest = np.zeros((10, self.duration))

        # Initialisation des termes dans chaque matrice
        for i in range(10):
            self.matrix = np.array(
                [ContextualMapping_Consume[i], ContextualMapping_Flee[i], ContextualMapping_Random[i],
                 ContextualMapping_Rest[i]])
            self.matrix = self.matrix / np.sum(self.matrix)
            self.matrix_consume[i][0] = self.matrix[0]
            self.matrix_flee[i][0] = self.matrix[1]
            self.matrix_random[i][0] = self.matrix[2]
            self.matrix_rest[i][0] = self.matrix[3]

    def update(self, new_elements_consume, new_elements_flee, new_elements_random, new_elements_rest, t):
        # Vérification de la taille des nouvelles listes d'éléments
        if len(new_elements_consume) != 10 or len(new_elements_flee) != 10 or len(new_elements_random) != 10 or len(
                new_elements_rest) != 10:
            print("Erreur : Les listes d'éléments doivent avoir une taille de 10.")
            return

        # Ajout des nouveaux éléments dans chaque matrice
        for i in range(10):
            self.n_matrix = np.array(
                [new_elements_consume[i], new_elements_flee[i], new_elements_random[i],
                 new_elements_rest[i]])
            self.n_matrix = self.n_matrix / np.sum(self.n_matrix)
            self.matrix_consume[i][t] = self.n_matrix[0]
            self.matrix_flee[i][t] = self.n_matrix[1]
            self.matrix_random[i][t] = self.n_matrix[2]
            self.matrix_rest[i][t] = self.n_matrix[3]


ante_reliability = AnteReliability([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                   [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                                   [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                                   [31, 32, 33, 34, 35, 36, 37, 38, 39, 40], 100)

new_elements_consume = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
new_elements_flee = [111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
new_elements_random = [121, 122, 123, 124, 125, 126, 127, 128, 129, 130]
new_elements_rest = [131, 132, 133, 134, 135, 136, 137, 138, 139, 140]

ante_reliability.update(new_elements_consume, new_elements_flee, new_elements_random, new_elements_rest, 1)
