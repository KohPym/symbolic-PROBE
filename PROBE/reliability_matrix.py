class AnteReliability:
    def __init__(self, ContextualMapping_Consume, ContextualMapping_Flee, ContextualMapping_Random, ContextualMapping_Rest):
        self.ContextualMapping_Consume = ContextualMapping_Consume
        self.ContextualMapping_Flee = ContextualMapping_Flee
        self.ContextualMapping_Random = ContextualMapping_Random
        self.ContextualMapping_Rest = ContextualMapping_Rest
        
        # Création des matrices de 1 colonne et 10 lignes
        self.matrix_consume = [[0] for _ in range(10)]
        self.matrix_flee = [[0] for _ in range(10)]
        self.matrix_random = [[0] for _ in range(10)]
        self.matrix_rest = [[0] for _ in range(10)]
        
        # Initialisation des termes dans chaque matrice
        for i in range(10):
            self.matrix_consume[i][0] = ContextualMapping_Consume[i]
            self.matrix_flee[i][0] = ContextualMapping_Flee[i]
            self.matrix_random[i][0] = ContextualMapping_Random[i]
            self.matrix_rest[i][0] = ContextualMapping_Rest[i]
