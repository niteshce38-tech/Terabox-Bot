import os
import requests
import telebot

TOKEN = "8816180255:AAECJ0hMs7ry7B859oRCvCvV1AUXrCwGAcg"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  user_name = message.from_user.first_name
  welcome_text = (
      f"👋 Hello {user_name}!\n\n"
      "🤖 Main TeraBox Downloader Bot hoon.\n"
      "🔗 Mujhe koi bhi TeraBox link bhejein, main video download link nikal"
      " kar deta hoon!"
  )
  bot.reply_to(message, welcome_text)


@bot.message_handler(
    func=lambda message: message.text
    and ("terabox" in message.text.lower() or "1024tera" in message.text)
)
def handle_terabox(message):
  url = message.text.strip()
  msg = bot.reply_to(
      message, "⏳ Terabox link process ho raha hai, thoda intezaar karein..."
  )

  try:
    # Free Public Terabox API request
    api_url = (
        f"https://terabox-dl-api.complexcoders.workers.dev/?url={url}"  # Public API
    )
    # Alternately, hum direct link parsing handle karenge
    bot.edit_message_text(
        "📥 Video link extract kiya ja raha hai...",
        message.chat.id,
        msg.message_id,
    )

    # Yahan hum ek alternative reliable free API endpoint use karenge
    r = requests.get(
        f"https://tera-dl.yanz.workers.dev/api?url={url}", timeout=20
    ).json()

    if r and "download_url" in r:
      down_link = r["download_url"]
      file_name = r.get("file_name", "video.mp4")

      caption = (
          f"✅ **Download Successful!**\n\n📁 **File:** {file_name}\n🔗 [Direct"
          f" Download Link]({down_link})"
      )
      bot.edit_message_text(
          caption, message.chat.id, msg.message_id, parse_mode="Markdown"
      )
    else:
      # Agar direct link API se na aaye toh alternative format
      bot.edit_message_text(
          "⚠️ Direct download link nahi mil paya. Terabox ki security ki"
          " wajah se yeh link block ho gaya hai.",
          message.chat.id,
          msg.message_id,
      )

  except Exception as e:
    bot.edit_message_text(
        "❌ Error: Video fetch karne mein samasya aayi. Dobara try karein.",
        message.chat.id,
        msg.message_id,
    )


@bot.message_handler(func=lambda message: True)
def default_text(message):
  bot.reply_to(message, "⚠️ Kripya ek valid TeraBox link bhejein.")


print("Bot running...")
bot.polling()
