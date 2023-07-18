import numpy as np

def transition_matrix(states, num_states=4):
    """
    Crée une matrice de transition à partir d'une liste de séquences d'états.
    
    Args:
    - states : une liste de séquences d'états
    - num_states : le nombre total d'états (par défaut 4)
    
    Returns:
    - la matrice de transition
    """
    # Initialiser la matrice de transition avec des zéros
    transition_mat = np.zeros((num_states, num_states))

    # Compter les transitions entre les états
    for state_seq in states:
        for i in range(len(state_seq)-1):
            from_state = state_seq[i]
            to_state = state_seq[i+1]
            transition_mat[from_state][to_state] += 1

    # Normaliser les lignes pour obtenir une matrice de probabilité
    row_sums = transition_mat.sum(axis=1)
    transition_mat = transition_mat / row_sums[:, np.newaxis]

    return transition_mat


states = [[0, 1, 2, 1, 3], [3, 2, 1, 0, 1, 2, 3]]
transition_mat = transition_matrix(states)
print(transition_mat)

[[0.         0.5        0.25       0.25      ]
 [0.33333333 0.         0.33333333 0.33333333]
 [0.2        0.4        0.         0.4       ]
 [0.25       0.25       0.25       0.25      ]]
