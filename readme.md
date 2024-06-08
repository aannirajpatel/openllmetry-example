# LangChain OpenLLMetry Example

This is an example of how to use the OpenLLMetry package to instrument your LLM application and send traces, metrics, and logs to an OpenTelemetry http backend.

## Requirements

- Python 3.10+ installed on your machine
    - Repository tested with [Python 3.11.5](https://www.python.org/downloads/release/python-3115/)
- An IDE, preferably [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Steps

The instructions for each step are located in the `instructions` directory. Each step has its own markdown file with detailed instructions on what to do:
1. [Step 1](instructions/step-1.md) - Setup the project with Pipenv and add the necessary packages to the project.
1. [Step 2](instructions/step-2.md) - Create an LLM application using LangChain and FastAPI.
1. [Step 3](instructions/step-3.md) - Add some opinionated observability instrumentation to the LLM application using OpenLLMetry.

The code for each step is in its own branch. The main branch contains the final version of the code.