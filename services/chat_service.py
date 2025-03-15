import os
import google.generativeai as genai
from chat.prompts import get_system_prompt

class ChatService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_DEV_API_KEY")
        self.messages = []
        if not self.api_key:
            print("Gemini API key not found!")
            exit(1)

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.messages = [
            {"role": "user", "parts": [self.get_system_prompt()]}
        ]
        self.chat_session = self.model.start_chat(history=self.messages)

    def get_system_prompt(self):
        return get_system_prompt()

    def chat(self, message):
        try:
            response = self.chat_session.send_message(message)
            return response.text
        except Exception as e:
            print(e)
