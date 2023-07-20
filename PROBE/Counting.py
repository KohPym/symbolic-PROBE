import numpy as np

def counting_matrix(num_states=5, fill_value=0):
    """
    Crée une matrice de comptage pour compter les transitions entre les états.

    Args:
    - num_states : le nombre total d'états (par défaut 5)
    - fill_value : la valeur avec laquelle remplir la matrice (par défaut 0)

    Returns:
    - la matrice de comptage remplie de fill_value
    """
    # Initialiser la matrice de comptage avec des zéros ou avec fill_value si spécifié
    count_mat = np.full((num_states, num_states), fill_value, dtype=int)

    # Créer un dictionnaire pour faire la correspondance entre les noms d'états et leurs indices
    state_names = ["Consume", "Flee", "Rest", "Stock", "Random"]
    state_dict = {name: i for i, name in enumerate(state_names)}

    return count_mat, state_dict


def update_counting_matrix(count_mat, state_dict, from_state_name, to_state_name):
    """
    Met à jour la matrice de comptage en fonction d'une transition entre deux états.
    
    Args:
    - count_mat : la matrice de comptage
    - state_dict : le dictionnaire de correspondance entre les noms d'états et leurs indices
    - from_state_name : le nom de l'état de départ
    - to_state_name : le nom de l'état d'arrivée
    
    Returns:
    - la matrice de comptage mise à jour
    """
    # Récupérer les indices correspondant aux noms d'états
    from_state = state_dict[from_state_name]
    to_state = state_dict[to_state_name]

    # Incrémenter l'élément de la matrice de comptage correspondant à la transition
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
