import shutil
import os
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from agent import agent

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

class DocQuery(BaseModel):
    file_id: str
    text: str

@app.get('/')
def read_root():
    return {"status": "Agent API is online"}

@app.post('/ask')
async def ask_agent(query: UserQuery):
    try:
        # Call agent logic from agent.py
        print(query)
        result = await agent.get_web_response(query.text)
        return result
    except Exception as e:
        print(f"Web Search Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_id = await agent.process_file(temp_path)
        return {"file_id": file_id, "filename": file.filename}
    except Exception as e:
        print(f"File Upload Error: {e}")
        raise HTTPException(status_code=500, detail='Failed to process file.')
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.post('/ask-doc')
async def ask_doc(query: DocQuery):
    print(f"Doc Query: {query}")
    try:
        result = await agent.get_doc_response(query.file_id, query.text)
        return result
    except Exception as e:
        print(f"Doc Query Error: {e}")
        raise HTTPException(status_code=500, detail='Error querying the document.')