import os
from traceloop.sdk import Traceloop
from opentelemetry.instrumentation.openai import OpenAIInstrumentor


def setup_openllmetry():
    Traceloop.init(
        "arithmetic_service",
        api_endpoint=os.getenv("OTLP_ENDPOINT"),
        headers={"Authorization": os.getenv("OTLP_AUTHORIZATION_HEADER")},
    )
    OpenAIInstrumentor().instrument()
