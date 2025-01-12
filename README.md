# AI Assistant Project

This project provides a command-line ai tools that can be used for various tasks including code explanation, review, and chat. It utilizes OpenAI's API to leverage the capabilities of AI models.

## Features

- Interactive command-line interface.
- Supports multiple roles: Chat, Explain, Review.
- Easy integration through environment variables and prompts.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install required Python packages:
   ```bash
   pip install python-dotenv openai
   ```

3. Add the project directory to your PATH with:
   ```bash
   ./install.sh
   ```

4. Set up your `.env` file to store API keys:
   ```env
   CHAT_API_KEY=your_chat_api_key
   EXPLAINER_API_KEY=your_explainer_api_key
   REVIEWER_API_KEY=your_reviewer_api_key
   ```

## Usage

- To chat with the AI Assistant:
   ```bash
   ask
   ```

- To get explanations from the AI:
   ```bash
   curl -I example.com | explain
   ```

   ```bash
   explain "packages in python"
   ```

   ```bash
   explain < input.txt
   ```

- To review code:
   ```bash
   review < ai_assistant.py
   ```
