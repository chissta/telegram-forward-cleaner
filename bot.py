
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor

API_TOKEN = '7742793435:AAEfiDRqV3l93abwRdbGVkewSbOl6UcH1rM'
CHANNEL_ID = -1001396133180  # آیدی عددی کانال شما

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=ContentType.ANY)
async def repost_clean(message: types.Message):
    if message.chat.id == CHANNEL_ID and (message.forward_from_chat or message.forward_from):
        try:
            if message.text:
                await bot.send_message(CHANNEL_ID, message.text)
            elif message.photo:
                await bot.send_photo(CHANNEL_ID, message.photo[-1].file_id, caption=message.caption)
            elif message.video:
                await bot.send_video(CHANNEL_ID, message.video.file_id, caption=message.caption)
            elif message.document:
                await bot.send_document(CHANNEL_ID, message.document.file_id, caption=message.caption)
            elif message.animation:
                await bot.send_animation(CHANNEL_ID, message.animation.file_id, caption=message.caption)
            elif message.audio:
                await bot.send_audio(CHANNEL_ID, message.audio.file_id, caption=message.caption)
            # حذف پیام اصلی
            await bot.delete_message(CHANNEL_ID, message.message_id)
        except Exception as e:
            print(f"Error processing message: {e}")

if __name__ == '__main__':
    executor.start_polling(dp)
