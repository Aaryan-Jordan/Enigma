# Enigma

**Enigma** is an innovative, privacy-focused **local AI assistant** that empowers your desktop experience. It combines virtual mouse control, powerful voice commands, and advanced automation to seamlessly manage files, emails, browsing, and much more. All intelligence runs locally—your data stays yours.

---

## ✨ Features

- **Virtual Mouse Control:** Operate your mouse (move, click, drag) via voice or gesture.
- **Voice-Powered Automation:** Natural language commands to:
  - Create, modify, or delete files and folders
  - Send emails
  - Search & play videos on YouTube
  - Scroll through reels and web feeds
  - Launch or control OS-level applications
- **Intelligent Local LLM:** Uses fine-tuned, locally-hosted LLMs for reliable command parsing and task execution.
- **Hardcoded OS Actions:** Secure, robust OS integrations—file management, application control, clipboard tasks, and more.
- **Privacy-First:** No online processing; all AI models and scripts execute on your machine.
- **Modular & Extensible:** Easily add new voice actions or automation workflows.

---

## 🚀 Installation

### Prerequisites

- **Python 3.8** or newer
- **Git**
- **Pip** (Python package manager)
- Microphone (for voice commands)
- (Optional but recommended) Nvidia GPU for fast LLM/speech inference

### Steps

1. **Clone the repository:**
git clone https://github.com/Aaryan-Jordan/Enigma.git
cd Enigma

text

2. **Install dependencies:**
pip3 install -r requirements.txt
*(Typical dependencies: `pyautogui`, `openai-whisper` or `faster-whisper`, `llama-cpp-python`, `speechrecognition`, `selenium`, etc.)*

3. **Download or point to your local LLM model**
- Place your fine-tuned LLM in the `models/` directory, or specify its path in the `config.yaml`.

4. **Configure email/automation credentials (for advanced features)**
- See `config.yaml` and fill in any local details as needed for Gmail API, etc.

5. **Run Enigma:**

---

## 💻 Usage

After launching, interact with Enigma by **speaking commands** or using the provided UI/CLI (if available):

- **General Usage Examples:**
- "Move the mouse to the top right and click."
- "Open my Documents folder."
- "Create a new file called meeting_notes.txt."
- "Email the latest report to my manager."
- "Search lo-fi music on YouTube and play the first result."
- "Scroll through Instagram reels."

*Enigma interprets your requests and automates the actions using local models and scripts.*

---

## 🛠 Architecture & Tech Stack

- **Speech-to-Text:** [Whisper](https://github.com/openai/whisper) (or compatible local models)
- **Large Language Model:** [Llama](https://github.com/facebookresearch/llama), [Gemma](https://ai.google.dev/gemma), etc., locally fine-tuned
- **Virtual Mouse & Automation:** `pyautogui`, `opencv-python`, `mediapipe`
- **Email**: `smtplib` for SMTP or Gmail API (local only)
- **Web Automation:** `selenium`, `pyautogui` for UI tasks
- **Hardcoded OS Scripts:** OS-level Python/bash scripts for reliability

---

## 📂 Project Structure

Enigma/
│
├── main.py # Program entry point
├── enigma/ # Core modules (voice, llm, automation, mouse, etc.)
├── requirements.txt # Python dependencies
├── config.yaml # User config for LLM, email, etc.
├── models/ # Local LLM and STT models
└── README.md
