# Instructions for Step 2

In this step, we will create an LLM application using LangChain and FastAPI. The application will act as an AI agent that can use a calculator to perform simple arithmetic operations. We will expose this agent as an API using FastAPI.

First we need to prototype and build the AI agent using LangChain. We will utilize jupyter notebooks for this purpose, and then move the code to a python file.

To use jupyter notebook functionality, we need to install the following packages:
```bash
pipenv install notebook
```

Next, we will launch the jupyter notebook server using the following command:
```bash
pipenv run jupyter notebook
```

This will open a new tab in your browser with the jupyter notebook interface. Create a new notebook named `prototyping.ipynb` and start building the AI agent.

Once the AI agent is created, add an endpoint in `main.py` to use the AI agent to perform arithmetic operations. To keep things simple, we will use a GET endpoint and pass the prompt as a query parameter. The request URL will look something like this and you can run this in your browser with the app running:
```
localhost:8080/calculate?prompt=What is 2 plus 2?
```

Finally, we port the code to create the agent into a file `agent.py` and import the agent into the endpoint handler in `main.py`.