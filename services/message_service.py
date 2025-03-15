import json
import os
import constants

class MessageService:
    def __init__(self):
        print("Initiated message service")


    def handleMessage(self, message):
        self.updateTempResponseFile(message)
        self.executeCommands()


    def updateTempResponseFile(self, message):
        try:
            content = message.split("```json")[-1].strip("````").strip()
            with open(constants.TEMP_RESPONSE_FILE_NAME, "w") as file:
                file.write(content)
        except Exception as e:
            print(e)


    def getOutputData(self):
        try:
            data = None
            with open(constants.TEMP_RESPONSE_FILE_NAME) as file:
                data = json.load(file)

            return data
        except Exception as e:
            print(e)


    def executeCommands(self):
        try:
            data = self.getOutputData()
            commands = data['output']

            for cmdObj in commands:
                cmd = cmdObj['command']
                os.system(cmd)
        except Exception as e:
            print(e)