import os
import telebot

# Aapka token yahan set hai
TOKEN = "8816180255:AAECJOhMs7ry7B8S9oRCvCvViAUXrCWGAcg"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(
      message,
      "👋 Hello! Paste Your Terabox Link Here",
  )


@bot.message_handler(func=lambda message: "terabox" in message.text.lower())
def handle_link(message):
  url = message.text
  bot.reply_to(message, f"Link mil gaya: {url}")


print("Bot shuru ho gaya hai...")
bot.polling()
