from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Merhaba, Render çalışıyor!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
import os
import telegram
from flask import Flask, request

app = Flask(__name__)

# Token'i environment'tan çekiyoruz
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route("/")
def home():
    return "Bot çalışıyor 🚀"

# Test için sana mesaj gönderen bir endpoint
@app.route("/send_test")
def send_test():
    chat_id = "SENIN_CHAT_ID"  # Buraya kendi chat id gelecek
    bot.send_message(chat_id=chat_id, text="Merhaba! Bot başarılı şekilde Render’da çalışıyor 🚀")
    return "Mesaj gönderildi ✅"
