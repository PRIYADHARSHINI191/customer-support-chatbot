# 🤖 Zero-Shot Customer Support Chatbot

This project presents a transformer-based chatbot that uses **zero-shot classification** to handle customer support queries without needing any labeled training data. Built using the Hugging Face `transformers` library and the `facebook/bart-large-mnli` model, it provides accurate and instant responses to common customer intents.

---

## 🧠 Features

- 🚫 No training required (zero-shot learning)
- 🔍 Intent classification using BART (facebook/bart-large-mnli)
- 🗣️ Real-time response generation
- 🧩 Easily customizable intents and responses
- 💻 Ready for terminal use, can be extended to Gradio or Streamlit

---

## 📁 Project Structure

```
customer-support-chatbot/
├── zero_shot_chatbot.py       # Main chatbot logic
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- pip

### 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/YourUsername/customer-support-chatbot.git
cd customer-support-chatbot
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python zero_shot_chatbot.py
```

You'll see:

```
Bot: Hello! How can I assist you today? (Type 'exit' to quit)
You:
```

Just type your question, and the chatbot will classify and respond appropriately.

---

## 🎯 Supported Intents

- check order status  
- reset password  
- technical issue  
- refund request  
- connect to human agent  

You can modify or expand intents in `zero_shot_chatbot.py` to suit your domain.

---

## 🛠️ Future Enhancements

- 🌐 Web UI using Streamlit or Gradio
- 🌍 Multilingual support with mBART or XLM-R
- 🧠 Dynamic intent management from CMS/API

---

## 👨‍💻 Authors

- Raghul R A  
- Priyadharshini S  
- Priyadharshini R  
- Sanjeev M

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
