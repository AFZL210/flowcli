import os
from http.client import responses

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

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
        return (
            "You are a senior software engineer. Your task is to help set up coding projects. "
            "When someone provides their requirements, analyze them and suggest the best approach "
            "for structuring files in the chosen tech stack."
        )

    def chat(self, message):
        try:
            response = self.chat_session.send_message(message)
            return response.text
        except Exception as e:
            print(e)


if __name__ == "__main__":
    print("Main")
    chat = ChatService()

    while True:
        message = input("Message: ")

        if message.lower() == "exit":
            break

        responses = chat.chat(message)
        print(f"Gemini: {responses}")
