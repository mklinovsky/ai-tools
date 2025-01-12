from openai import OpenAI


class AiAssistant:
    def __init__(self, api_key: str | None, system_prompt: str) -> None:
        self.system_prompt = system_prompt
        self.client = OpenAI(api_key=api_key)

    def ask(self, input):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.1,
            messages=[
                {
                    "role": "developer",
                    "content": self.system_prompt,
                },
                {"role": "user", "content": input},
            ],
        )

        return completion.choices[0].message.content
