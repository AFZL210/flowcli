import json
from dotenv import load_dotenv
from services.chat_service import ChatService
load_dotenv()

temp_response_filename = 'temp-response.json'

def updateTempResponseFile(content):
    content = content.split("```json")[-1].strip("````").strip()
    with open(temp_response_filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    print("Main")
    chat = ChatService()

    while True:
        message = input("Message: ")

        if message.lower() == "exit":
            break

        response = chat.chat(message)
        updateTempResponseFile(response)
        print("Raw response", response)
