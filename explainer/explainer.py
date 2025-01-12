#!/usr/bin/env python3

from openai import OpenAI
import sys


def create_client():
    return OpenAI(
        api_key="",
    )


def get_input():
    return sys.stdin.read().strip()


def get_explanation(client, input):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "developer",
                "content": "You are a helpful technical assistant. Your task is to explain provided content. Your answer should be clear and conscise, epxlanation should be short and on point. Use only plain text, the response will be displayed in bash.",
            },
            {"role": "user", "content": input},
        ],
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    input = get_input()
    client = create_client()

    print("Original input:\n")
    print(input)
    print("\nGenerating AI response...\n")
    explanation = get_explanation(client, input)
    print(explanation)
