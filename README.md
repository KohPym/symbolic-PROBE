# PROBE Model

This is a computational implementation of the PROBE model with a perspective of implementing Symbolic data.
The model is applied to a survival task where an agent is supposed so survive taking care of his/her own statistics.

> [!NOTE]
> Statistics here refers to level of Health, Energy, Satiety, Hydration and Toxicity

# PROBE Folder

The PROBE folder is composed by Task Set required for the task: Consume, Flee, Random and Rest.
environment.py is the file which create the environment required for the survival task.
The biomes.py and food.py files are used to create the environment.

# Experiment operationalization

You can use the model by executing the main.py file only.
All subsequent structure can be modified but do not require to be executed.

```
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py 
```

# Task Set (TS) Folder (Pending Work)

Every TS folder has the same architecture. A TS is composed by three models: contextual, predictive and selective.
The selective model require an ontology file and an individual file to make the Reinforcement Symbolic Learning works.


