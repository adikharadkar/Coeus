import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

# Setup the Client
client = genai.Client(api_key=gemini_api_key)

# Configure the Search Tool
# This is the "Grounding" tool that gives the Gemini real-time web access
search_tool = types.Tool(google_search=types.GoogleSearch())

# Create the agentic chat
chat = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        tools=[search_tool],
        # System instructions set the "personality" and rules
        system_instruction="You are a realtime research assistant. Use Google Search for any current events or facts you aren't 100 percent sure about."
    )
)

def get_agent_response(user_message: str):
    print("--- Real-time Web Search Agent (Type 'exit' to quit) ---")

    while True:
        
        if (user_message.lower() in ["exit", 'quit']):
            break

        # The agent sends the message and automatically triggers search if needed
        response = chat.send_message(user_message)

        # Return the response
        return {
            "answer": response.text
        }

        # OPTIONAL: See exactly what the AI searched for and where it got the data
        # if response.candidates[0].grounding_metadata:
        #     metadata = response.candidates[0].grounding_metadata
        #     if metadata.search_entry_point:
        #         print("\n[Sources found via Google Search]")
        #         # In 2026, the metadata provides specific URLs used
        #         for chunk in metadata.grounding_chunks:
        #             if chunk.web:
        #                 print(f"- {chunk.web.title}: {chunk.web.url}")

