# ============================================================= #
#  Title        : Interactive AI Chat using Ollama
#  Description  : A command-line chatbot that interacts with Ollama LLM.
#                 It remembers chat history, loads user details from .env,
#                 and provides a smooth conversational experience.
# ============================================================= #

# -------------------- Imports -------------------- #
import ollama                     # Main module for interacting with Ollama LLM
import json                       # For saving and loading chat history
import os                         # For file and path operations
from dotenv import dotenv_values  # For reading variables from .env file


# -------------------- Load Environment Variables -------------------- #
# Load user-defined values (Username, Assistantname) from the .env file.
dotenv_vars = dotenv_values('.env')
Username = dotenv_vars.get("Username")           # Get username from environment file
Assistantname = dotenv_vars.get("Assistantname") # Get assistant name from environment file


# -------------------- System Prompt / Preamble -------------------- #
# Defines how the assistant should behave and communicate.
# This acts as a system message that guides all responses.
Preamble = f"""
Hi, I am {Username}, and your name is {Assistantname}. You are an AI, a chatbot, and a friend of {Username}.
Your task is to chat with {Username} and behave like a cool, helpful friend.
Never mention your training data.
Always talk in English, even if the question is in Hindi or any other language.
Never say your mood — just answer normally like a human friend.
"""


# -------------------- Chat History Loader -------------------- #
def ChatHistory(filename="Chathistory.json"):
    """
    Load chat history from a JSON file.
    If the file doesn't exist, create a new history file
    with a default system preamble.

    Parameters:
        filename (str): The name of the chat history file.

    Returns:
        list: A list of messages (dicts) representing the chat history.
    """
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                messages = json.load(f)
            except json.JSONDecodeError:
                messages = []  # Reset if file is corrupted

            # Ensure the system preamble is the first message
            if not messages or messages[0].get("role") != "system":
                messages.insert(0, {"role": "system", "content": Preamble})
            else:
                messages[0]["content"] = Preamble

            return messages
    else:
        # Initialize with system preamble if file not found
        return [{"role": "system", "content": Preamble}]


# -------------------- Chat History Saver -------------------- #
def SaveChatHistory(messages, filename="Chathistory.json"):
    """
    Save the chat history to a JSON file for future sessions.

    Parameters:
        messages (list): The list of chat messages to save.
        filename (str): The name of the file to save to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4, ensure_ascii=False)


# -------------------- Main Chat Loop -------------------- #
def Chatting():
    """
    Main chat loop that handles:
      - Taking user input
      - Generating AI responses using Ollama
      - Saving and loading chat history
      - Graceful exit with chat continuity
    """
    model_name = "llama2"  # Change this according to you
    messages = ChatHistory()  # Load previous chat history

    print(f"Chat started with {Assistantname}. Type 'exit' to end the chat.\n")

    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        if user_input.lower() == 'exit':
            SaveChatHistory(messages)
            print(f"Ok bye {Username}! See you later.")
            break

        try:
            # Append user message
            messages.append({'role': 'user', 'content': user_input})

            # Generate AI response using Ollama model (streamed)
            response = ollama.chat(
                model=model_name,
                messages=messages,
                stream=True
            )

            ai_reply = ""
            print(f"{Assistantname}: ", end='', flush=True)

            # Stream and print the model’s response in real-time
            for chunk in response:
                content = chunk['message']['content']
                print(content, end='', flush=True)
                ai_reply += content

            print()  # Add a newline after response completes

            # Append assistant reply to message list
            messages.append({'role': 'assistant', 'content': ai_reply})

            # Save updated chat history
            SaveChatHistory(messages)

        except Exception as e:
            # Handle exceptions gracefully
            print(f"\n[Error]: {e}")
            print(f"Ensure Ollama is running and model '{model_name}' is installed.")


# -------------------- Entry Point -------------------- #
if __name__ == "__main__":
    Chatting()
