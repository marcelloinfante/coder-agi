# Coder AGI
Coder AGI is a AI Coder Agent inspired by smol developer and EngineerGPT.

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
