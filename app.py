import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

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

bot.infinity_polling()
