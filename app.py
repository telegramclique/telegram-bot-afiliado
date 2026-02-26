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
    print("Bot iniciado com sucesso!")
    bot.infinity_polling()

@bot.message_handler(content_types=['text'])
def gerar_link(message):
    link = message.text.strip()
    codigo = "seucodigo123"

    print("Mensagem recebida:", link)

    if "http" in link:
        link_afiliado = f"{link}?tag={codigo}"
        resposta = f"🔥 Seu link afiliado:\n{link_afiliado}"
    else:
        resposta = "Envie um link começando com http ou https."

    bot.reply_to(message, resposta)

if __name__ == "__main__":
    threading.Thread(target=run).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
