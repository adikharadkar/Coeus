from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent import get_agent_response

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define what the incoming data should look like
class UserQuery(BaseModel):
    text: str

@app.get('/')
def read_root():
    return {"status": "Agent API is online"}

@app.post('/ask')
async def ask_agent(query: UserQuery):
    try:
        # Call agent logic from agent.py
        print(query)
        result = get_agent_response(query.text)
        return result
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail='The agent encounters an error')