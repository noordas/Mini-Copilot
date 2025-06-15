# Mini-Copilot
Mini Copilot is an AI-powered coding and documentation assistant built with Streamlit and OpenAI GPT-4. It helps in boosting dev productivity with AI.


# Mini Copilot – Coding & Documentation Assistant

Mini Copilot is an AI-powered assistant built using **Streamlit** and **OpenAI GPT-4** to supercharge developer productivity.

With a simple and intuitive interface, it enables:
-  **Code generation** from natural language
-  **Code explanation** line-by-line
-  **Auto-generation of documentation** for better handovers and onboarding



## Live Demo

> Coming soon – deploy to Streamlit Cloud or run locally (instructions below).




## Tech Stack

| Component        | Tool            |
|------------------|------------------|
| Backend AI       | OpenAI GPT-4     |
| Frontend UI      | Streamlit        |
| Language         | Python 3.10+     |
| Secrets Manager  | python-dotenv    |


## Features

Generate Python code from a natural prompt  
Explain existing code clearly and line-by-line  
Auto-generate documentation (docstrings or markdown)  
Fast response via OpenAI's ChatCompletion API  
Clean, minimal UI with Streamlit


## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/noordas/mini-copilot.git
cd mini-copilot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your-api-key-here
```

> You can get an API key from: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

### 4. Run the App
```bash
streamlit run app.py
```

---

##  Example Prompts

| Feature | Prompt Example |
|--------|----------------|
| Generate Code | `Write a Python function to check if a number is prime.` |
| Explain Code | `def fib(n): return 1 if n<=2 else fib(n-1)+fib(n-2)` |
| Generate Docs | (Paste any Python code for auto-documentation) |

---

##  Folder Structure

```
mini-copilot/
├── app.py
├── .env.example
├── requirements.txt
├── mini_copilot_presentation.pptx
└── README.md
```

---

## Future Improvements

-  GitHub repo integration for large projects  
-  Voice input via Whisper API  
-  Deployment to Streamlit Cloud or Vercel  
-  Save/load prompt history  

---

##  Author

**Bhilla Noordhas** – AI Intern at Planto.ai  
🔗 [LinkedIn](https://www.linkedin.com/in/noordhas-bhilla-5b5626256?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

