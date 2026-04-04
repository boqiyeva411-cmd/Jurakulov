from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.reply import main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        f"👋 Assalomu alaykum, **{message.from_user.full_name}**!\n\n"
        "🚀 Men **Professional Python Developer**man.\n"
        "Ushbu bot orqali mening ishlarim bilan tanishishingiz va loyiha buyurtma berishingiz mumkin."
    )
    await message.answer(welcome_text, reply_markup=main_menu(), parse_mode="Markdown")