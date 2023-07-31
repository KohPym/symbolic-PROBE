import numpy as np

class CountingMatrix:
    def __init__(self, num_states=4, fill_value=1):
        """
        Initialize a counting matrix with the given number of states and fill value.

        Args:
            num_states (int): Total number of states, default value is 4.
            fill_value (int): Number to fill the matrix with, default value is 1. It increases virtually the initial impact of first transitions.
        """
        self.count_mat = np.full((num_states, num_states), fill_value, dtype=int)
        self.state_names = ["Consume", "Flee", "Rest", "Stock", "Random"]
        self.state_dict = {name: i for i, name in enumerate(self.state_names)}

    def update(self, from_state_name, to_state_name):
        """
        Update the counting matrix to apply the change/transition between states.

        Args:
            from_state_name (str): Name of the starting state.
            to_state_name (str): Name of the ending state.

        Returns:
            The updated counting matrix.
        """
        from_state = self.state_dict[from_state_name]
        to_state = self.state_dict[to_state_name]
        self.count_mat[from_state][to_state] += 1
        return self.count_mat



# Créer la matrice de comptage et le dictionnaire de correspondance entre les noms d'états et leurs indices
count_mat, state_dict = counting_matrix()

# Effectuer une transition de l'état "Consume" à l'état "Flee"
count_mat = update_counting_matrix(count_mat, state_dict, "Consume", "Flee")

# Effectuer une transition de l'état "Flee" à l'état "Random"
count_mat = update_counting_matrix(count_mat, state_dict, "Flee", "Random")

# Afficher la matrice de comptage mise à jour
print(count_mat)

[[0 1 0 0 0]
 [0 0 0 0 1]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]
