# 🤖 AI Chat Terminal — Powered by Ollama LLM

A fully functional **command-line AI chatbot** built using the **Ollama Large Language Model (LLM)** framework.  
It provides real-time, human-like conversations, remembers your chat history, and adapts its personality dynamically using environment variables.

---

## 🧭 Overview

This project lets you **chat with a personalized AI assistant** directly from your terminal —  
no cloud, no API keys, and complete privacy.

The chatbot uses **local models from Ollama**, and its identity (name, tone, behavior) is defined by your `.env` file.  
It’s like having your own private ChatGPT running locally on your machine.

---

## ✨ Features

✅ **Real-time conversation** with Ollama  
✅ **Personalized AI name and user identity** from `.env`  
✅ **Persistent chat memory** (`Chathistory.json`)  
✅ **Streaming responses** (word-by-word output)  
✅ **Offline operation** (no API keys or cloud needed)  
✅ **Error handling** for model or system failures  
✅ **Clean, documented, and GitHub-ready code**

---

## ⚙️ How It Works

1. Loads your `Username` and `Assistantname` from a `.env` file.
2. Uses these to generate a **custom system prompt** (personality & behavior).
3. Stores your chats in `Chathistory.json` for continuity.
4. Connects to **Ollama** locally to generate real-time responses.
5. Saves everything automatically for the next session.

---

AI-Chat-Terminal/
│
├── main.py # Main chatbot code
├── Chathistory.json # Chat history file
├── .env # User and assistant configuration
├── requirements.txt # Python dependencies (optional)
├── LICENSE # Project license (MIT recommended)
└── README.md # This file

## 🧰 Requirements

- Python **3.10+**
- [Ollama](https://ollama.ai/download) installed locally
- VS Code
- Any supported model (like `llama2`, `phi3`, `mistral`, or `qwen2`)

---

## Installation 
1. Download the zip file
2. extract it
3. open it with vs code

## Install Dependencies
pip install ollama python-dotenv

run PrivateAI.py

enjoy



## 🧩 Project Structure

