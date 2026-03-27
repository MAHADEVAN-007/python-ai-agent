# 🤖 Python AI Agent

This is a simple AI-powered research assistant I built using **Groq + LangChain**.
The idea is straightforward — you ask a question, and the agent tries to give a clean, structured answer, even using the web when needed.

---

## 🚀 What it can do

* Answer general questions
* Search the web for up-to-date info
* Return responses in a structured format (not messy text)
* Keep things fast using Groq (LLaMA models)

---

## 🛠 Tech used

* Python
* LangChain
* Groq API
* Pydantic

---

## 📁 Project structure

```bash
python-ai-agent/
│
├── main.py
├── requirements.txt
├── .gitignore
└── .env (not included)
```

---

## ⚙️ How to run it

### 1. Clone the repo

```bash
git clone https://github.com/MAHADEVAN-007/python-ai-agent.git
cd python-ai-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the project

```bash
python main.py
```

---

## 💡 Example

**Input:**

```
What is ransomware?
```

**Output (simplified):**

```
Topic: Ransomware

Summary:
A type of malware that locks or encrypts data and demands money to unlock it.

Sources:
- FBI
- Microsoft
```

---

## 🧠 How it works (simple version)

* You enter a query
* The agent decides if it needs to search the web
* It generates an answer
* The response is formatted into a clean structure

---

## 🔧 Things I can improve later

* Add memory (chat history)
* Build a web interface
* Add more tools (APIs, calculator, etc.)
* Improve response quality

---

## 👨‍💻 Author

Raman Mahadevan
GitHub: https://github.com/MAHADEVAN-007

---

If you find this useful, feel free to ⭐ the repo.
