from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "7058988325:AAGlcTEeHHThACMwT-I8RlVSZqIk687pyNI"
TARGET_USER_ID = 1394753930

bot = Bot(token=TOKEN)
application = ApplicationBuilder().token(TOKEN).build()

async def forward_to_target(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message.text:
        await bot.send_message(chat_id=TARGET_USER_ID, text=f"📩 Сообщение от @{update.effective_user.username or 'неизвестного'}:\n{message.text}")
    elif message.photo:
        await bot.send_photo(chat_id=TARGET_USER_ID, photo=message.photo[-1].file_id, caption=f"🖼 Фото от @{update.effective_user.username or 'неизвестного'}")
    elif message.video:
        await bot.send_video(chat_id=TARGET_USER_ID, video=message.video.file_id, caption=f"🎥 Видео от @{update.effective_user.username or 'неизвестного'}")
    elif message.audio:
        await bot.send_audio(chat_id=TARGET_USER_ID, audio=message.audio.file_id, caption=f"🎵 Аудио от @{update.effective_user.username or 'неизвестного'}")
    elif message.voice:
        await bot.send_voice(chat_id=TARGET_USER_ID, voice=message.voice.file_id, caption=f"🎤 Голосовое от @{update.effective_user.username or 'неизвестного'}")
    elif message.document:
        await bot.send_document(chat_id=TARGET_USER_ID, document=message.document.file_id, caption=f"📄 Файл от @{update.effective_user.username or 'неизвестного'}")
    else:
        await bot.send_message(chat_id=TARGET_USER_ID, text="🗂 Неизвестный тип сообщения.")
    await message.reply_text("✅ Отправлено! Спасибо за мемчик 😉")

application.add_handler(MessageHandler(filters.ALL, forward_to_target))

WEBHOOK_URL = "https://frotbig.onrender.com" + TOKEN

application.run_webhook(
    listen="0.0.0.0",
    port=10000,
    webhook_url=WEBHOOK_URL
)
