# LangChain OpenLLMetry Example

This is an example of how to use the OpenLLMetry package to instrument your LLM application and send traces, metrics, and logs to an OpenTelemetry http backend.

## Requirements

- Python 3.10+ installed on your machine
    - Repository tested with [Python 3.11.5](https://www.python.org/downloads/release/python-3115/)
- An IDE, preferably [Visual Studio Code](https://code.visualstudio.com/download) with the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Steps

The instructions for each step are located in the `instructions` directory. Each step has its own markdown file with detailed instructions on what to do.

The code for each step is in its own branch. The main branch contains the final version of the code.

1. Branch `step-1` - Setup the project with Pipenv and add langchain, fastapi, and openllmetry packages.
1. Branch `step-2` - Create an LLM application - we will create a LangChain app that acts as an AI agent which can use a calculator to perform simple arithmetic operations. We will expose this agent as an API using FastAPI.
1. Branch `step-3` - Instrument the LLM application with OpenLLMetry - we will add some opinionated instrumentation using OpenLLMetry to the LLM application to send traces, metrics, and logs to an OpenTelemetry http backend.