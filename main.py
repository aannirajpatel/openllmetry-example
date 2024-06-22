from fastapi import FastAPI
from dotenv import load_dotenv
from agent import agent_executor
from otel import setup_openllmetry

load_dotenv()
app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}


@app.get("/calculate")
def calculate(
    prompt: str | None = "what is 11241 plus 534235.222 minus 153252 "
    "multiplied by 11",
):
    return {"result": agent_executor.invoke({"input": prompt})}
setup_openllmetry(app)