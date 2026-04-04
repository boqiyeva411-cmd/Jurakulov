import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import start, menu, contact

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Routerni ulash
    dp.include_routers(
        start.router, 
        menu.router, 
        contact.router
    )

    print("--- Bot ishga tushdi ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")