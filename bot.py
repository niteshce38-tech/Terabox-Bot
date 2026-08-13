
import os
import telebot

TOKEN = "8816180255:AAECJ0hMs7ry7B859oRCvCvV1AUXrCwGAcg"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  user_name = message.from_user.first_name
  welcome_text = (
      f"👋 Hello {user_name}!\n\n"
      "🤖 Main aapka **TeraBox Downloader Bot** hoon.\n"
      "🔗 Mujhe koi bhi TeraBox link bhejein!"
  )
  bot.reply_to(message, welcome_text, parse_mode="Markdown")


@bot.message_handler(
    func=lambda message: message.text
    and ("terabox" in message.text.lower() or "1024tera" in message.text)
)
def handle_terabox(message):
  url = message.text.strip()
  # User ko message bhejo ki link mil gaya hai
  bot.reply_to(
      message,
      f"📥 **TeraBox Link Received!**\n\n🔗 `{url}`\n\n*(Note: Video file"
      " fetch karne ke liye bot ka parsing engine active ho raha hai)*",
      parse_mode="Markdown",
  )


@bot.message_handler(func=lambda message: True)
def default_text(message):
  bot.reply_to(message, "⚠️ Kripya mujhe ek valid **TeraBox Link** bhejein.")


print("Bot successfully run ho raha hai...")
bot.polling()
