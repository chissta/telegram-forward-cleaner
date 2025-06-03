
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7742793435:AAEfiDRqV3l93abwRdbGVkewSbOl6UcH1rM"
CHANNEL_ID = -1001396133180

async def handle_forwarded(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if message.forward_date:
        try:
            await message.delete()
            if message.photo:
                file_id = message.photo[-1].file_id
                await context.bot.send_photo(chat_id=CHANNEL_ID, photo=file_id, caption=message.caption)
            elif message.video:
                file_id = message.video.file_id
                await context.bot.send_video(chat_id=CHANNEL_ID, video=file_id, caption=message.caption)
            elif message.text:
                await context.bot.send_message(chat_id=CHANNEL_ID, text=message.text)
            elif message.caption:
                await context.bot.send_message(chat_id=CHANNEL_ID, text=message.caption)
        except Exception as e:
            print(f"خطا: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & filters.Chat(chat_id=CHANNEL_ID), handle_forwarded))
    app.run_polling()
