from dotenv import load_dotenv
from services.chat_service import ChatService
from services.message_service import MessageService
load_dotenv()

if __name__ == "__main__":
    chatService = ChatService()
    messageService = MessageService()

    while True:
        message = input("Message: ")

        if message.lower() == "exit":
            break

        response = chatService.chat(message)
        messageService.handleMessage(response)
