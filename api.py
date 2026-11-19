from fastapi import FastAPI
from pydantic import BaseModel
from agents.workflow import Workflow
app=FastAPI(title='ForgeAgents')
class Task(BaseModel):
    task: str
    use_ollama: bool = False
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/run')
def run(task: Task): return Workflow(llm=task.use_ollama).run(task.task)
