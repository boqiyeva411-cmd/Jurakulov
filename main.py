import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiohttp import web
from config import TOKEN
from handlers import start, menu, contact

# --- Render uchun kichik HTTP server qismi ---
async def handle(request):
    return web.Response(text="Bot ishlayapti!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Render avtomatik beradigan PORT ni oladi, bo'lmasa 10000
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logging.info(f"Web server {port} portida ishga tushdi")

# --- Asosiy Bot qismi ---
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

    # Render port xatosini oldini olish uchun serverni parallel ishga tushiramiz
    asyncio.create_task(start_web_server())

    print("--- Bot ishga tushdi ---")
    
    # Pollingni boshlash
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi")