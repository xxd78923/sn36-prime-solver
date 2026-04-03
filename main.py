from fastapi import FastAPI, Body
from agent import handle_act
app = FastAPI(title="sn36-prime-solver")
@app.post("/act")
async def act(p: dict = Body(...)): return {"actions": await handle_act(**p)}
