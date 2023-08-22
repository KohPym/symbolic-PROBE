# PROBE Model

This is a computational implementation of the PROBE model with a perspective of implementing Symbolic data.

# Experiment type

The task is a survival task where an agent is supposed so survive taking care of his/her own statistics.
> [!NOTE]
> Statistics here refers to level of Health, Energy, Satiety, Hydration and Toxicity

# PROBE Folder

The PROBE folder is composed by the Task Set required for the task: Consume, Flee, Random and Rest.
environment.py is the file which create the environment required for the survival task.
The biomes.py and food.py files are used to create the environment.

# Experiment operationalization

You can use the model by executing the main.py file only.
All subsequent structure can be modified but do not require to be executed.

# Task Set (TS) Folder

Every TS folder has the same architecture. A TS is composed by three models: contextual, predictive and selective.
The selective model require an ontology file and an individual file to make the Reinforcement Symbolic Learning works.

- 
