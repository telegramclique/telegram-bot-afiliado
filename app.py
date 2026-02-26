import os
import telebot
from flask import Flask
from threading import Thread

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot online!"

@bot.message_handler(func=lambda message: True)
def gerar_link(message):
    link_original = message.text
    seu_codigo = "seucodigo123"

    if "amazon" in link_original:
        link_afiliado = link_original + "?tag=" + seu_codigo
        resposta = f"🔥 Seu link de afiliado:\n{link_afiliado}"
    else:
        resposta = "Envie um link válido."

    bot.reply_to(message, resposta)


def iniciar_bot():
    bot.infinity_polling(timeout=10, long_polling_timeout=5)


if __name__ == "__main__":
    Thread(target=iniciar_bot).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, threaded=True)
