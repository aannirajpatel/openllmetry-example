# Instructions for Step 1

In this step, we will setup the project with Pipenv and add the necessary packages to the project.

We will also set up a FastAPI HTTP endpoint that returns a simple "Hello World" message.

To get started, create a new directory for the project and change into the project directory:
```bash
# Create a new directory for the project
mkdir langchain-openllmetry-example
# Change into the project directory
cd langchain-openllmetry-example
# Install pipenv
pip install pipenv
# Initialize a new Pipenv project
pipenv install
# Install the required packages
pipenv install langchain langchain-openai fastapi traceloop-sdk opentelemetry-instrumentation-openai
```

Next, create a new file named `main.py` in the project directory and add the following code to it:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

This code sets up a FastAPI application with a single endpoint that returns a JSON response with a "Hello World" message.

To run the FastAPI application, use the following command from the repository root:
```bash
pipenv run uvicorn main:app --reload
```