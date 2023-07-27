# Coder AGI
Coder AGI is a AI Coder Agent inspired by smol developer, EngineerGPT, Chain Of Thought Paper, ReAct Paper and Tree Of Thought Papers.

## Arquitecture
1. The Planner Agent plan all the actions that should be taken.
2. The first objective of the plan is executed by the executer agent.
3. The action of the executer agent is evaluated by the evaluator agent.
4. If the action is successfull:
   1. Then all the files created are commited to save the state.
   2. The executer goes to the next objetive
5. Else:
   1. Git rollback to the initial state of the action.
   2. The executer uses chain of thought to try a new action with the feedback of the evaluator.
   3. If the executer fail 5 times, the planner will think a plan to continue the execution
6. The execution wil continue until all the objetices are sucessfully completed.
  

 ## Quick Start
 1. Create a python virtual environment.
```
python -m venv venv
```

 2. Activate the virtual environment.
```
# Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

 3. Install the dependencies
```
pip install -r requirements.txt
```

 4. Add a .env file and add your OpenAI api key
```
# .env
OPENAI_API_KEY=....
```

 5. Add the model and the app description of you project config.json file
```
# config.json
{
  "model": "gpt-3.5-turbo-16k",
  "app_description": "Create a django application for a blog api",
  "max_steps": 200
}
```

 6. Run the agent
```
python main.py
```
