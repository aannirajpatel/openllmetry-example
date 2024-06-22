import os
from traceloop.sdk import Traceloop
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

def setup_openllmetry(app):
    Traceloop.init(
        "arithmetic_service",
        api_endpoint=os.getenv("OTLP_ENDPOINT"),
        headers={"Authorization": os.getenv("OTLP_AUTHORIZATION_HEADER")},
    )
    FastAPIInstrumentor.instrument_app(app=app)
    OpenAIInstrumentor().instrument()
