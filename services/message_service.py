import json
import subprocess
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
            print(f"Error updating response file: {e}")

    def getOutputData(self):
        try:
            with open(constants.TEMP_RESPONSE_FILE_NAME) as file:
                return json.load(file)
        except Exception as e:
            print(f"Error reading response file: {e}")
            return None

    def executeCommands(self):
        try:
            data = self.getOutputData()
            if not data:
                print("No commands to execute.")
                return

            command_script = "\n".join([cmdObj["command"] for cmdObj in data["output"]])

            script_path = constants.RESPONSE_SCRIPT_FILE_NAME
            with open(script_path, "w") as script_file:
                script_file.write(f"#!/bin/bash\nsource ~/.nvm/nvm.sh\n{command_script}\nexec bash")

            subprocess.run(["chmod", "+x", script_path])

            subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"{script_path}"])

        except Exception as e:
            print(f"Error executing commands: {e}")
