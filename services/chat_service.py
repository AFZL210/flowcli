import os
from pyexpat.errors import messages

import google.generativeai as genai
import constants
from chat.prompts import get_system_prompt

class ChatService:
    def __init__(self):
        self.messages, self.chat_session = self.setup()


    def setup(self):
        api_key = os.getenv(constants.GEMINI_API_KEY_NAME)
        if not api_key:
            print("Gemini API key not found!")
            exit(1)
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(constants.GEMINI_MODEL)
        messages = [{"role": "user", "parts": [get_system_prompt()]}]
        chat_session = model.start_chat(history=messages)

        return messages, chat_session


    def chat(self, message):
        try:
            response = self.chat_session.send_message(message)
            return response.text
        except Exception as e:
            print(e)



