import os
import time
import sys
from datetime import datetime
from dotenv import load_dotenv
from ai_assistant import AiAssistant


class AssistantCreator:
    def __init__(
        self,
        api_key_name: str,
        system_prompt_file_name: str,
        assistant_name: str,
        interactive=False,
    ) -> None:
        load_dotenv()

        self.interactive = interactive
        self.assistant_name = assistant_name

        api_key = os.getenv(api_key_name)
        system_prompt = self.read_system_prompt(system_prompt_file_name)

        self.ai_assistant = AiAssistant(api_key, system_prompt)

    def get_input(self):
        if self.interactive:
            input_data = input("🤖 >> ").strip()
        else:
            input_data = (
                sys.argv[1]
                if len(sys.argv) > 1 and sys.argv[1]
                else sys.stdin.read().strip()
            )

        return input_data

    def read_system_prompt(self, file_name):
        prompt_path = self.get_current_path(file_name)

        with open(prompt_path, "r") as file:
            system_prompt = file.read()

        return system_prompt

    def get_current_path(self, file_name):
        dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(dir, file_name)

    def write_response(self, response):
        file = self.get_current_path("last_response.md")
        with open(file, "w") as file:
            file.write(response)

    def track(self, input, response, duration):
        file = self.get_current_path("responses.md")
        with open(file, "a") as file:
            file.write(
                f"{self.get_line("🤓", "prompt", input)}{self.get_line("🤖", "response", f'{response}\n\n{duration} s')}"
            )

    def get_line(self, icon, type, text):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{'---\n\n' if type == 'prompt' else ''}{icon} [{self.assistant_name}] {type} ({current_time})\n\n{text}\n\n"

    def ask(self):
        input = self.get_input()

        start_time = time.time()
        response = self.ai_assistant.ask(input)
        duration = round(time.time() - start_time, 2)

        print(input)
        print("\n========== 🤖 ==========\n")
        print(response)
        print(f"\n{ duration } s")

        self.write_response(response)
        self.track(input, response, duration)
