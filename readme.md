# LangChain OpenLLMetry Example

This is an example of how to use the OpenLLMetry package to instrument your LLM application and send traces, metrics, and logs to an OpenTelemetry http backend.

Each step is subdivided into branches, so you can follow along with the changes made in each step.

This main branch contains the final version of the code.

## Steps

Branch `step-1` - Setup the project with Pipenv and add langchain, fastapi, and openllmetry packages.

Branch `step-2` - Create an LLM application - we will create a LangChain app that acts as an AI agent which can use a calculator to perform simple arithmetic operations. We will expose this agent as an API using FastAPI.

Branch `step-3` - Instrument the LLM application with OpenLLMetry - we will add OpenLLMetry instrumentation to the LLM application to send traces, metrics, and logs to an OpenTelemetry http backend.