from certifi import contents

import constants

class MessageService:
    def __init__(self):
        print("Initiated message service")


    def handleMessage(self, message):
        self.updateTempResponseFile(message)


    def updateTempResponseFile(self, message):
        content = message.split("```json")[-1].strip("````").strip()
        with open(constants.TEMP_RESPONSE_FILE_NAME, "w") as file:
            file.write(content)