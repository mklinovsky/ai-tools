import os
from dotenv import load_dotenv
import sys
from ai_assistant import AiAssistant


class AssistantCreator:
    def __init__(self, api_key_name: str, system_prompt_file_name: str) -> None:
        load_dotenv()

        api_key = os.getenv(api_key_name)
        system_prompt = self.read_system_prompt(system_prompt_file_name)

        self.ai_assistant = AiAssistant(api_key, system_prompt)

    def get_input(self):
        return (
            sys.argv[1]
            if len(sys.argv) > 1 and sys.argv[1]
            else sys.stdin.read().strip()
        )

    def read_system_prompt(self, file_name):
        dir = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(dir, file_name)

        with open(prompt_path, "r") as file:
            system_prompt = file.read()

        return system_prompt

    def ask(self):
        input = self.get_input()
        response = self.ai_assistant.ask(input)

        print(input)
        print("\n========== AI response ==========\n")
        print(response)
