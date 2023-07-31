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
