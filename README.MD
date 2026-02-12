# AI Interviewer

A Python project that simulates an AI-based interview using **Google Gemini** via the LangChain library. The AI asks role-specific and level-specific interview questions, evaluates answers, and provides feedback.

---

## Features

- Generates **interview questions** based on role and difficulty level.
- Collects user answers and provides **AI-generated scores and feedback**.
- Supports multiple roles like Python Developer, Data Analyst, etc.
- Adjustable difficulty: `easy`, `medium`, `hard`.

---

## Requirements

- Python 3.10 or higher
- Install required packages using:

```bash
pip install -r requirements.txt
A .env file with your Google API key:

GOOGLE_API_KEY=your_api_key_here
How to Run

Clone the repository:

git clone https://github.com/username/repo-name.git
cd repo-name

Ensure your .env file is configured.

Run the AI Interviewer:

python ai_interviewer.py

Enter your role and difficulty level when prompted.

Answer the AI-generated questions and see instant feedback.