from environment import Environment
from agent import Agent

# Creation of the seed to insure reproducibility
seed = 12
# Setting for the print option (readability purpose essentially)
np.set_printoptions(suppress=True, precision=2)

# Choice of the number of observation period. This refers to the number of biomes observed by the agent.
# In others words, this means the prior knowledge on biome and the potential (satiety, hydration etc) of each biome.
observation_period = int(input("Enter the number of observation periods (between 100 and 100000): "))
# Creation of the observation matrix in which all the information of the current biome, food (...) is stock.
observation = ObservationMatrix()
# The matrix is accessible at any time using "observation.matrix".

# Creation of observation data
for _ in range(observation_period):
    survival_env = Environment()  # Instantiation of the environment class.
    survival_env.choose_biome()  # Biome and biomes attributes are is chosen.
    # We can access to the information of the current biome with "survival_env.current_biome"
    survival_env.choose_food()  # Selection of food depending on the requirement of the biome.
    # e.g. that we can not have an apple in a Desert.
    # We can access to the information of the selected food with "survival_env.current_food"
    survival_env.multiply_food()  # Creation of random number of food inside the chosen biome.
    # This to insure the biome not to be monotonous and helps to be depleted.
    survival_env.choose_predation()  # This will create the level of predation of the current biome.
    # e.g. the level of dangerousness coming from the fauna.
    survival_env.summary_matrix()  # Matrix summarizing the whole information of the current biome, predation
    # and linked foods.
    observation.update(decode_biome(survival_env.current_biome['name']), survival_env.predation_level,
                       survival_env.summary_matrix()[-1])
    # Update the observation matrix using the current biome as index through the use of the "decode_biome" function.
    observation.normalize_matrix()  # Normalize the matrix element to be ranged into probabilities and used in
    # reliabilities function.


# Just to take a look at the result of the observation session:
print(observation.matrix)
print(observation.norm_matrix)

# After the observation and the "knowledge" of the environment is created, we can create the agent and the main loop.
agent_bob = Agent(delta=2, health=50, energy=80, satiety=80, hydration=80, toxicity=0)
# These stats are default value in the agent.py file, and are not necessary but written for showing purpose.
# "delta" value can be confusing but mainly refer to the difficulty of the environment (between 1 and 3 included).
# e.g. how toxicity infer on health, how quick energy decrease ...

# Choice of the agent aversion to risk. This will increase the apprehension of predation level.
risk_aversion = float(input("Enter the agent's aversion to risk (a number between 0 and 100): "))
# Choice of the experiment period. This refers to the number of task set selection the agent will face.
experiment_period = int(input("Enter the experiment period t (between 100 and 100000): "))
# Choice of the learning rate inferring on the speed the agent will learn between each time step.
learning_rate = 0.01
# Choice of the total_timesteps for the learning of each of Reinforcement Symbolic Learning algorithm.
total_timesteps = 10000
# Choice of the discount_factor for the learning of each of Reinforcement Symbolic Learning algorithm.
discount_factor = 0.5
# Choice of the radius of spreading information inside the Reinforcement Symbolic Learning algorithm.
radius = 0.001
# Training of each of the Reinforcement Symbolic Learning algorithms based on each different ontologies for
# each task set:

################################################ NOT WORKING FOR NOW ################################################

# sm_consume.SelectiveModel_Consume().train_symbolic_qlearning(total_timesteps, learning_rate, discount_factor, radius,
                                    # log_name=f"runs/symbolic-ql-{r}")
# sm_flee.SelectiveModel_Flee().train_symbolic_qlearning(total_timesteps, learning_rate, discount_factor, radius,
                                    # log_name=f"runs/symbolic-ql-{r}")
# sm_random.SelectiveModel_Random().train_symbolic_qlearning(total_timesteps, learning_rate, discount_factor, radius,
                                    # log_name=f"runs/symbolic-ql-{r}")
# sm_rest.SelectiveModel_Rest().train_symbolic_qlearning(total_timesteps, learning_rate, discount_factor, radius,
                                    # log_name=f"runs/symbolic-ql-{r}")

####################################################################################################################

for t in range(experiment_period):
    # Initial structure is the same as previously (e.g. observation) as we create biome but now, the agent will do
    # things rather than purely observe. Also, agent's stats will be modified in time.
    survival_env = Environment()
    survival_env.choose_biome()
    survival_env.choose_food()
    survival_env.multiply_food()
    survival_env.choose_predation()
    survival_env.summary_matrix()

    if t == 0:
        observation_consume = np.mean(observation.norm_matrix[:, 0:3], axis=1, keepdims=True)
        # Definition of the variable corresponding of the three first columns of the observation matrix.
        # e.g. consumption essentials: Satiety, Hydration and Vitamins level.
        # NOTE: This take actually the mean of these three columns but can be completely adjusted.
        # This is why this part is not hardcoded inside a function somewhere else.
        ante_reliability_consume = cm_consume.AnteReliability_Consume(observation_consume)
        # This allows the Consume task set to get some information of the agent on every biome observed.
        # This serves as first "contextual mapping" as we are in a task with prior observation.
        observation_flee = np.reshape(observation.norm_matrix[:, 5], (-1, 1))
        # Variable for the observation of predation level, used to compute the contextual mapping for flee task set.
        ante_reliability_flee = cm_flee.AnteReliability_Flee(observation_flee)
        # This allows the Flee task set to get the mean level of predation of each biome observed.
        observation_random = np.mean(observation.norm_matrix[:, [0,1,2,5]], axis=1, keepdims=True)
        # Ditto but for random task set, then taking the mean of each level. This is completely assumed to be arbitrary
        # and can be changed for further improvements/tests.
        ante_reliability_random = cm_random.AnteReliability_Random(observation_random)
        observation_rest = (1 - np.reshape(observation.norm_matrix[:, 5], (-1, 1)))
        # Ditto for rest task set, focusing on predation level.
        ante_reliability_rest = cm_rest.AnteReliability_Rest(observation_rest)

        lambda_matrix = AnteReliability(ante_reliability_consume.contextual_mapping,
                                        ante_reliability_flee.contextual_mapping,
                                        ante_reliability_random.contextual_mapping,
                                        ante_reliability_rest.contextual_mapping, experiment_period)
        # The lambda_matrix represent exactly the prior reliability of each task set.
        # It is composed by 4 matrix (1 per task set) each of them of size 10 (number of biomes) per experiment_period
        # (decided above). Each of the reliability is a probability and normalized according to others task set for
        # the same biome at a specific time step.

        lambda_list = [lambda_matrix.matrix_consume[decode_biome(survival_env.current_biome['name'])][t],
                       lambda_matrix.matrix_flee[decode_biome(survival_env.current_biome['name'])][t],
                       lambda_matrix.matrix_random[decode_biome(survival_env.current_biome['name'])][t],
                       lambda_matrix.matrix_rest[decode_biome(survival_env.current_biome['name'])][t]]
        # Creation of the list of the lambda implied in the actual environment. This refers to the probability of
        # each task set for this time step, in the current biome after the process of normalization between task set.
        max_lambda = max(lambda_list) # To obtain the maximum of these probabilities.
        best_task_set = lambda_list.index(max_lambda) # In order to map the best probability with the task set.
        # NOTE: To give us an idea of the task set preferred we can look at "decode_task_set(best_task_set)".

        # We then select the correct task set and thus, the selective model associated.
        # Inside the selective model can be find the ontology associated to the task set, the individuals objects
        # on which the algorithm will be applied and finally the Reinforcement Symbolic Learning part.
        selective_models = {
            0: sm_consume,
            1: sm_flee,
            2: sm_random,
            3: sm_rest
        }
        if best_task_set in selective_models:
            action = selective_models[best_task_set](np.argmax(model.qtable[tuple(observation)]))
            # We get the best action to do inside the correct task set.
        else:
            print("Incorrect number") # This "else" condition is not only to prevent a problem on the index but also
            # to propose a way of implementing a PROBE task set. This part of the structure helps to create a
            # potentially new task set.
        action_probability = ? # Probability linked to the best action chose by the RSL algorithm.
        individual = 'Elderberry'  # Individual item on which action was done

        ############################################ REPLACEMENT STRUCTURE ############################################

        action = 1
        action_probability = 0.5
        individual = 'Elderberry'

        ###############################################################################################################

        selective_action = {
            0: Consume,
            1: Flee,
            2: Rest,
            3: doNothing
        }
        # Here, we get the action used inside the task set, to be mapped with the number in order to make the
        # environment and the agent stat's change.
        # The rules are that is something is "consumed", the quantity diminished by one.
        # If the agent flee or rest, the environment then change.
        # If nothing is done, then, the agent stay in the actual biome.

        if selective_action[action] == "Consume":
            matching_name = None
            k = 0
            for item in survival_env.current_food:
                k += 1
                name = item['name']
                if individual == name:
                    matching_name = name
                    break

            agent_bob.modify_health()
            agent_bob.modify_energy()
            agent_bob.modify_satiety()
            agent_bob.modify_hydration()
            agent_bob.modify_toxicity()

            # survival_env.depletion() # This is a function to deplete the environment, actually not used.
        elif selective_action[action] == "Flee" or selective_action[action] == "Rest":
            survival_env = Environment() # Not used for now as without every tool, the env change whatever the action
            # is done
        else:
            print("Nothing")


        agent_bob.update()
        score = homeostasis(agent_bob.health, agent_bob.energy, agent_bob.satiety, agent_bob.hydration,
                            agent_bob.toxicity)

        calcul des mus
