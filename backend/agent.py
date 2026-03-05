import os
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=gemini_api_key)

search_tool = types.Tool(google_search=types.GoogleSearch())

class HybridAgent:
    def __init__(self):
        self.chat = client.chats.create(
            model='gemini-2.5-flash',
            config=types.GenerateContentConfig(
                tools=[search_tool],
                system_instruction="You are a realtime research assistant. Use Google Search for any current events or facts you aren't 100 percent sure about."
            )
        )

    async def get_web_response(self, user_message: str):
        print(f"User Message: {user_message}")
        response = self.chat.send_message(user_message)
        return {"answer": response.text}
    
    async def process_file(self, file_path: str):
        uploaded_file = client.files.upload(file=file_path)

        while uploaded_file.state.name == "PROCESSING":
            time.sleep(2)
            uploaded_file = client.files.get(name=uploaded_file.name)

        return uploaded_file.name
    
    async def get_doc_response(self, file_id: str, user_message: str):
        active_file = client.files.get(name=file_id)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[active_file, user_message],
            config=types.GenerateContentConfig(
                system_instruction='You are analyzing a private document. Only answer based on the provided file.'
            )
        )
        return {"answer": response.text}

agent = HybridAgent()