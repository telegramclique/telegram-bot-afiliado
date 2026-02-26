import telebot
import os
from flask import Flask
import threading

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot está rodando!"

def run_bot():
    bot.infinity_polling()

@bot.message_handler(func=lambda message: True)
def gerar_link(message):
    link_original = message.text
    seu_codigo = "seucodigo123"

    if "amazon" in link_original:
        link_afiliado = link_original + "?tag=" + seu_codigo
        resposta = f"🔥 Seu link de afiliado:\n{link_afiliado}"
    else:
        resposta = "Envie um link válido da Amazon."

    bot.reply_to(message, resposta)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
