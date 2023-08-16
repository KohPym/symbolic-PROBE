from agent import *
from environment import Environment
from observation_matrix import ObservationMatrix
from decoder import *
import numpy as np
from reliability_matrix import *
import glob
from transition_matrix import *
import importlib.util
from Consume import contextual_model_consume as cm_consume
from Consume import predictive_model_consume as pm_consume
from Flee import contextual_model_flee as cm_flee
from Flee import predictive_model_flee as pm_flee
from Random import contextual_model_random as cm_random
from Random import predictive_model_random as pm_random
from Rest import contextual_model_rest as cm_rest
from Rest import predictive_model_rest as pm_rest

# folder_paths = ['..', '../Consume', '../Flee', '../Random', '../Rest', '../Stock']
# for folder_path in folder_paths:
#     file_paths = glob.glob(os.path.join(folder_path, '*.py'))
#     for file_path in file_paths:
#         file_name = os.path.splitext(os.path.basename(file_path))[0]
#         module = __import__(f'{folder_path}.{file_name}')
#         classes = [cls for cls in module.__dict__.values() if isinstance(cls, type)]

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

tau = TransitionMatrix(num_states=4, fill_value=1)
previous_action = 'Rest'
action_probability = np.zeros(4)
sedentary_score = 0
homeostasis_score = np.ones(experiment_period + 1)
homeostasis_score[0] = homeostasis(agent_bob.health, agent_bob.energy, agent_bob.satiety, agent_bob.hydration,
                                   agent_bob.toxicity)

for t in range(experiment_period):
    # Initial structure is the same as previously (e.g. observation) as we create biome but now, the agent will do
    # things rather than purely observe. Also, agent's stats will be modified in time.
    if previous_action != 'Consume':
        survival_env = Environment()
        survival_env.choose_biome()
        survival_env.choose_food()
        survival_env.multiply_food()
        survival_env.choose_predation()
        survival_env.summary_matrix()
    else:
        sedentary_score += 1 # Help to look how much time the agent choose to stay on an environment

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

        # The same way, we create the initial post_reliability values. They are initialized only to be created and
        # not to infer at the beginning (because there is not any previous action for now).
        post_reliability_consume = pm_consume.PostReliability_Consume(np.ones((10, 1)))
        post_reliability_flee = pm_flee.PostReliability_Flee(np.ones((10, 1)))
        post_reliability_random = pm_random.PostReliability_Random(np.ones((10, 1)))
        post_reliability_rest = pm_rest.PostReliability_Rest(np.ones((10, 1)))

        lambda_matrix = AnteReliability(ante_reliability_consume.contextual_mapping,
                                        ante_reliability_flee.contextual_mapping,
                                        ante_reliability_random.contextual_mapping,
                                        ante_reliability_rest.contextual_mapping, experiment_period)
        # The lambda_matrix represent exactly the prior reliability of each task set.
        # It is composed by 4 matrix (1 per task set) each of them of size 10 (number of biomes) per experiment_period
        # (decided above). Each of the reliability is a probability and normalized according to others task set for
        # the same biome at a specific time step.
        mu_matrix = PostReliability(experiment_period) # We proceed the same for mu_matrix representing the
        # post reliability matrix. This means the probability after an action and task set has been taken.

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
        # Inside the selective model can be found the ontology associated to the task set, the individuals objects
        # on which the algorithm will be applied and finally the Reinforcement Symbolic Learning part.
        ###############################################################################################################
        # selective_models = {
        #     0: sm_consume,
        #     1: sm_flee,
        #     2: sm_random,
        #     3: sm_rest
        # }
        # if best_task_set in selective_models:
        #     action = selective_models[best_task_set](np.argmax(model.qtable[tuple(observation)]))
            # We get the best action to do inside the correct task set.
        # else:
        #     print("Incorrect number") # This "else" condition is not only to prevent a problem on the index but also
            # to propose a way of implementing a PROBE task set. This part of the structure helps to create a
            # potentially new task set.
        # action_probability = selective_models[best_task_set]. # Probability linked to the best action chose by the
        # RSL algorithm.
        # individual = selective_models[best_task_set].  # Individual item on which action was done

        # selective_action = {
        #     0: Consume,
        #     1: Flee,
        #     2: Rest,
        #     3: doNothing
        # }

        # if selective_action[action] == "Consume":
        #     matching_name = None
        #     k = 0
        #     for item in survival_env.current_food:
        #         k += 1
        #         name = item['name']
        #         if individual == name:
        #             matching_name = name
        #             break
        #
        #     agent_bob.modify_health()
        #     agent_bob.modify_energy()
        #     agent_bob.modify_satiety()
        #     agent_bob.modify_hydration()
        #     agent_bob.modify_toxicity()

            # survival_env.depletion() # This is a function to deplete the environment, actually not used.
        # elif selective_action[action] == "Flee" or selective_action[action] == "Rest":
        #     survival_env = Environment() # Not used for now as without every tool, the env change whatever the action
            # is done
        # else:
        #     print("Nothing")
        ###############################################################################################################

        ############################################ REPLACEMENT STRUCTURE ############################################

        selective_action = {
            0: 'Consume',
            1: 'Flee',
            2: 'Random',
            3: 'Rest'
        }

        tau.update(previous_action, selective_action[best_task_set])
        tau.normalize()

        previous_action = selective_action[best_task_set]

        depleted_matrix = survival_env.summary_matrix()[-1][:4]
        for i in range(4):
            depleted_matrix[i] /= survival_env.summary_matrix()[-1][4]

        if previous_action == 'Consume':
            agent_bob.modify_energy(depleted_matrix[2])
            agent_bob.modify_satiety(depleted_matrix[0])
            agent_bob.modify_hydration(depleted_matrix[1])
            agent_bob.modify_toxicity(depleted_matrix[3])
        elif previous_action == 'Rest':
            agent_bob.modify_health(depleted_matrix[0])
            agent_bob.modify_energy(20)
        else:
            agent_bob.modify_energy(-1)

        for j in range(4):
            if j == best_task_set:
                action_probability[j] = 0.7
            else:
                action_probability[j] = 0.1



        agent_bob.update()

        homeostasis_score[t+1] = homeostasis(agent_bob.health, agent_bob.energy, agent_bob.satiety, agent_bob.hydration,
                            agent_bob.toxicity)

        post_reliability_consume.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                   action_probability[0], t+1)
        post_reliability_flee.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                action_probability[1], t+1)
        post_reliability_random.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                  action_probability[2], t+1)
        post_reliability_rest.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                action_probability[3], t+1)

        new_mu_consume = post_reliability_consume.update_mu(
            ante_reliability_consume.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_consume.predictive_mapping)

        new_mu_flee = post_reliability_flee.update_mu(
            ante_reliability_flee.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_flee.predictive_mapping)

        new_mu_random = post_reliability_random.update_mu(
            ante_reliability_random.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_random.predictive_mapping)

        new_mu_rest = post_reliability_rest.update_mu(
            ante_reliability_rest.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_rest.predictive_mapping)

        mu_matrix.update(new_mu_consume, new_mu_flee, new_mu_random, new_mu_rest, t)

    else:

        ante_reliability_consume.update_contextual(
            decode_biome(survival_env.current_biome['name']),
            post_reliability_consume.predictive_mapping[decode_biome(survival_env.current_biome['name'])],
            learning_rate)
        ante_reliability_flee.update_contextual(
            decode_biome(survival_env.current_biome['name']),
            post_reliability_flee.predictive_mapping[decode_biome(survival_env.current_biome['name'])],
            learning_rate)
        ante_reliability_random.update_contextual(
            decode_biome(survival_env.current_biome['name']),
            post_reliability_random.predictive_mapping[decode_biome(survival_env.current_biome['name'])],
            learning_rate)
        ante_reliability_rest.update_contextual(
            decode_biome(survival_env.current_biome['name']),
            post_reliability_rest.predictive_mapping[decode_biome(survival_env.current_biome['name'])],
            learning_rate)

        new_mu_list = [post_reliability_consume.predictive_mapping[decode_biome(survival_env.current_biome['name'])],
                       post_reliability_flee.predictive_mapping[decode_biome(survival_env.current_biome['name'])],
                       post_reliability_random.predictive_mapping[decode_biome(survival_env.current_biome['name'])],
                       post_reliability_rest.predictive_mapping[decode_biome(survival_env.current_biome['name'])],]

        new_lambda_consume = ante_reliability_consume.update_lambda(
            ante_reliability_consume.contextual_mapping,
            decode_biome(survival_env.current_biome['name']),
            tau.prob_mat[0],
            new_mu_list)

        new_lambda_flee = ante_reliability_flee.update_lambda(
            ante_reliability_flee.contextual_mapping,
            decode_biome(survival_env.current_biome['name']),
            tau.prob_mat[1],
            new_mu_list)

        new_lambda_random = ante_reliability_random.update_lambda(
            ante_reliability_random.contextual_mapping,
            decode_biome(survival_env.current_biome['name']),
            tau.prob_mat[2],
            new_mu_list)

        new_lambda_rest = ante_reliability_rest.update_lambda(
            ante_reliability_rest.contextual_mapping,
            decode_biome(survival_env.current_biome['name']),
            tau.prob_mat[3],
            new_mu_list)

        lambda_matrix.update(new_lambda_consume, new_lambda_flee, new_lambda_random, new_lambda_rest, t)

        lambda_list = [lambda_matrix.matrix_consume[decode_biome(survival_env.current_biome['name'])][t],
                       lambda_matrix.matrix_flee[decode_biome(survival_env.current_biome['name'])][t],
                       lambda_matrix.matrix_random[decode_biome(survival_env.current_biome['name'])][t],
                       lambda_matrix.matrix_rest[decode_biome(survival_env.current_biome['name'])][t]]

        max_lambda = max(lambda_list) # To obtain the maximum of these probabilities.
        best_task_set = lambda_list.index(max_lambda) # In order to map the best probability with the task set.


        selective_action = {
            0: 'Consume',
            1: 'Flee',
            2: 'Random',
            3: 'Rest'
        }

        tau.update(previous_action, selective_action[best_task_set])
        tau.normalize()

        previous_action = selective_action[best_task_set]

        depleted_matrix = survival_env.summary_matrix()[-1][:4]
        for i in range(4):
            depleted_matrix[i] /= survival_env.summary_matrix()[-1][4]

        if previous_action == 'Consume':
            agent_bob.modify_energy(depleted_matrix[2])
            agent_bob.modify_satiety(depleted_matrix[0])
            agent_bob.modify_hydration(depleted_matrix[1])
            agent_bob.modify_toxicity(depleted_matrix[3])
        elif previous_action == 'Rest':
            agent_bob.modify_health(depleted_matrix[0])
            agent_bob.modify_energy(20)
        else:
            agent_bob.modify_energy(-1)

        for j in range(4):
            if j == best_task_set:
                action_probability[j] = 0.7
            else:
                action_probability[j] = 0.1

        agent_bob.update()

        homeostasis_score[t+1] = homeostasis(agent_bob.health, agent_bob.energy, agent_bob.satiety, agent_bob.hydration,
                            agent_bob.toxicity)

        post_reliability_consume.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                   action_probability[0], t+1)
        post_reliability_flee.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                action_probability[1], t+1)
        post_reliability_random.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                  action_probability[2], t+1)
        post_reliability_rest.update_predictive(decode_biome(survival_env.current_biome['name']), homeostasis_score,
                                                action_probability[3], t+1)

        new_mu_consume = post_reliability_consume.update_mu(
            ante_reliability_consume.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_consume.predictive_mapping)

        new_mu_flee = post_reliability_flee.update_mu(
            ante_reliability_flee.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_flee.predictive_mapping)

        new_mu_random = post_reliability_random.update_mu(
            ante_reliability_random.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_random.predictive_mapping)

        new_mu_rest = post_reliability_rest.update_mu(
            ante_reliability_rest.contextual_mapping[decode_biome(survival_env.current_biome['name'])],
            decode_biome(survival_env.current_biome['name']),
            post_reliability_rest.predictive_mapping)

        mu_matrix.update(new_mu_consume, new_mu_flee, new_mu_random, new_mu_rest, t)









        ###############################################################################################################


        # Here, we get the action used inside the task set, to be mapped with the number in order to make the
        # environment and the agent stat's change.
        # The rules are that is something is "consumed", the quantity diminished by one.
        # If the agent flee or rest, the environment then change.
        # If nothing is done, then, the agent stay in the actual biome.













        # We then apply a decision structure to introduce the interoception mechanism.
        # This guide the agent making choices not only based on the environment but also on the agent stats.
        # e.g. being hungry improve the usual probability of choosing the task set "Consume".






# def decision_structure(self, agent_energy, env_vitamins, agent_satiety, env_satiety, agent_hydration, env_hydration,
#                        agent_toxicity, env_toxicity, risk_aversion, env_predation):
#     predation_aversion = (70 * (2 - risk_aversion / 100)) / 1.4
#     if env_predation > predation_aversion:
#         return predation_aversion
#     else:
#         return env_predation
