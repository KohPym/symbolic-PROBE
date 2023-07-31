import numpy as np

class TransitionMatrix:
    def __init__(self, num_states=4, fill_value=1):
        """
        Initialize a counting matrix with the given number of states and fill value.

        Args:
            num_states (int): Total number of states, default value is 4.
            fill_value (int): Number to fill the matrix with, default value is 1. It increases virtually the initial impact of first transitions.
        """
        self.count_mat = np.full((num_states, num_states), fill_value, dtype=int)
        self.state_names = ["Consume", "Flee", "Random", "Rest", "NOT_USED_Stock"]
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
        
    def normalize(self):
        """
        Normalize the counting matrix to get a probability matrix.

        Returns:
            The probability matrix.
        """
        prob_mat = self.count_mat.astype(float) / np.sum(self.count_mat, axis=1, keepdims=True)
        return prob_mat
