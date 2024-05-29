import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from agent import agent_executor

load_dotenv()
app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}

@app.get("/calculate")
def calculate(prompt: str|None = "what is 11241 plus 534235.222 minus 153252 multiplied by 11"):
    return {"result": agent_executor.invoke({"input": prompt})}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8080)