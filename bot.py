import os
from threading import Thread
from flask import Flask
import telebot

TOKEN = "8816180255:AAECJOhMs7ry7B8S9oRCvCvViAUXrCWGAcg"
bot = telebot.TeleBot(TOKEN)

# Render Web Service ke liye chota sa Web Server
app = Flask("")


@app.route("/")
def home():
  return "Bot is running 24/7!"


def run_web():
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


# Telegram Bot Handlers
@bot.message_handler(commands=["start"])
def send_welcome(message):
  user_name = message.from_user.first_name
  bot.reply_to(
      message,
      f"👋 Hello {user_name}!\n\n🤖 Main TeraBox Downloader Bot hoon. Mujhe"
      " link bhejein!",
  )


@bot.message_handler(
    func=lambda message: message.text
    and ("terabox" in message.text.lower() or "1024tera" in message.text)
)
def handle_terabox(message):
  url = message.text.strip()
  bot.reply_to(
      message, f"📥 **Link Received:**\n`{url}`", parse_mode="Markdown"
  )


@bot.message_handler(func=lambda message: True)
def default_text(message):
  bot.reply_to(message, "⚠️ Kripya ek valid TeraBox link bhejein.")


if __name__ == "__main__":
  # Web server ko background thread mein start karein
  t = Thread(target=run_web)
  t.start()
  print("Bot aur Web Server successfully start ho gaye hain...")
  bot.polling()
