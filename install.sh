#!/usr/bin/env bash

AI_TOOLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ ":$PATH:" == *":$AI_TOOLS_DIR:"* ]]; then
    echo "The ai-tools folder is already in your PATH."
else
    echo "Adding $AI_TOOLS_DIR to your PATH..."
    echo "export PATH=\$PATH:$AI_TOOLS_DIR" >> "$HOME/.zshrc"
    echo "Added $AI_TOOLS_DIR to PATH in ~/.zshrc."
    echo "Please restart your terminal or run 'source ~/.zshrc' to apply changes."
fi
