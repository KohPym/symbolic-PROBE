import numpy as np

def create(num_states=4, fill_value=1):
    """
    Create a counting matrix in order to have a well designed transition matrix to evaluate the perceived volatility of each task sets.

    Args:
        num_states (int) -- Total number of states, default value is 4.
        fill_value (int) -- Number to fill the matrix with, default value is 1. It increase virtually the initial impact of first transitions.

    Returns:
        The counting matrix used to etablished the transition matrix.
    """
    count_mat = np.full((num_states, num_states), fill_value, dtype=int)
    state_names = ["Consume", "Flee", "Rest", "Stock", "Random"]
    state_dict = {name: i for i, name in enumerate(state_names)}
    return count_mat, state_dict


def update(count_mat, state_dict, from_state_name, to_state_name):
    """
    Update the transition matrix to apply the change/transition between states.
    
    Args:
        count_mat (matrix) -- Counting matrix to update
        state_dict (dict) -- The corresponding dictionnary between states and their index
        from_state_name (str) -- Name of the starting state
        to_state_name (str) -- Name of the ending state
    
    Returns:
        The updated counting matrix
    """
    from_state = state_dict[from_state_name]
    to_state = state_dict[to_state_name]
    count_mat[from_state][to_state] += 1
    return count_mat



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
