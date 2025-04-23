from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from catify import catify
import sqlite3
import os

app = Flask(__name__)

DB_PATH = "users.db"

# Opt-in and opt-out keywords (case-insensitive)
OPT_IN_KEYWORDS = {"start", "yes", "unstop"}
OPT_OUT_KEYWORDS = {"stop", "stopall", "unsubscribe", "quit", "cancel", "end"}

# Ensure the database and users table exist
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            phone_number TEXT PRIMARY KEY,
            opt_in INTEGER
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["POST"])
def sms_reply():
    """Respond to incoming messages based on opt-in status."""
    incoming_msg = request.form.get("Body", "").strip().lower()
    from_number = request.form.get("From", "")

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Check if user exists
    c.execute("SELECT opt_in FROM users WHERE phone_number = ?", (from_number,))
    row = c.fetchone()

    resp = MessagingResponse()

    if row is None:
        # New user – add them to the DB with opt_in = 0
        c.execute("INSERT INTO users (phone_number, opt_in) VALUES (?, ?)", (from_number, 0))
        conn.commit()
        msg = (
            "meowlo! 🐾 dis iz a mischievous cat!\n\n"
            "to talk 2 me, u gotta opt in 😼\n\n"
            "just text: start, yes, or unstop\n\n"
            "to stop hearin frum me, text: stop, stopall, unsubscribe, quit, cancel, or end"
        )
        resp.message(msg)
        conn.close()
        return str(resp)

    opted_in = row[0] == 1

    # Check for opt-in
    if incoming_msg in OPT_IN_KEYWORDS:
        c.execute("UPDATE users SET opt_in = 1 WHERE phone_number = ?", (from_number,))
        conn.commit()
        resp.message("yayyy! 🐱 we iz frens now. meow me anything~")
        conn.close()
        return str(resp)

    # Check for opt-out
    if incoming_msg in OPT_OUT_KEYWORDS:
        c.execute("UPDATE users SET opt_in = 0 WHERE phone_number = ?", (from_number,))
        conn.commit()
        resp.message("k byeeee... 🐾 no more meowz frum me. (text 'start' if u miss me...)")
        conn.close()
        return str(resp)

    # If not opted in yet
    if not opted_in:
        msg = (
            "meow! 😾 u gotta opt in b4 we talk.\n\n"
            "text: start, yes, or unstop\n\n"
            "to stop hearin frum me, text: stop, stopall, unsubscribe, quit, cancel, or end"
        )
        resp.message(msg)
        conn.close()
        return str(resp)

    # User is opted in – catify the message
    cat_response = catify(incoming_msg)
    resp.message(cat_response)
    conn.close()
    return str(resp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
