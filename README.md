# 🐾 Text-A-Cat SMS Bot

**Text-A-Cat** is a playful SMS bot that replies like a mischievous house cat! Built with Flask, OpenAI, and Twilio, this little feline lives to nap, sniff, and sass back in perfect paw-speak.

![cat typing](https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif)

---

## 🐱 What It Does

When someone texts your Twilio number, the bot responds with an AI-generated message in the voice of a goofy, curious, and somewhat judgmental house cat. It uses the OpenAI API (via `gpt-4o-mini`) to create delightfully weird responses that match your custom cat-brain prompt.

---

## ✨ Example

**Incoming SMS:**  
> What are you thinking about right now?

**Text-A-Cat Replies:**  
> mmmm... tuna... nap... chasing fluff! meeow!

---

## 🚀 Features

- 🧠 GPT-powered cat brain
- 📱 SMS support via Twilio
- 🐍 Built with Flask
- 🔐 Uses `.env` file to keep secrets safe

---

## ⚙️ Setup

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/text-a-cat.git
cd text-a-cat
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your environment variables**

Create a `.env` file:

```env
OPENAI_API_KEY=sk-your-api-key
TWILIO_ACCOUNT_SID=ACxxxxxxxx
TWILIO_AUTH_TOKEN=your_token
```

4. **Run it locally**

```bash
python app.py
```

Or with Gunicorn:

```bash
gunicorn -b 127.0.0.1:5000 app:app
```

---

## 🐾 Contributing

Want to teach the cat new tricks? Open a PR or meow at the issues tab.

---

## 📜 License

MIT — do what you want, just don't blame the cat.

---

## ❤️ Made with love, yarn, and AI

## 💵 Help fund this project to pay for Twilio and OpenAI! If I hit ~$20 a month, I will make my Text-a-Cat number public!
