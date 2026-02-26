import telebot
import os
from flask import Flask
import threading

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot online"

def run():
    print("Bot iniciado...")
    bot.infinity_polling()

@bot.message_handler(func=lambda message: True)
def gerar_link(message):
    link = message.text
    codigo = "seucodigo123"

    if link.startswith("http"):
        link_afiliado = f"{link}?tag={codigo}"
        bot.reply_to(message, f"🔥 Link afiliado:\n{link_afiliado}")
    else:
        bot.reply_to(message, "Envie um link válido.")

if __name__ == "__main__":
    threading.Thread(target=run).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
