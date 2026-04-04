from aiogram import Router, F, types
# Barcha kerakli inline klaviaturalarni tepada bir marta import qilamiz
from keyboards.inline import get_projects_inline, project_links, contact_inline

router = Router()

# --- 1. MEN HAQIMDA ---
@router.message(F.text == "🙋‍♂️ Men haqimda")
async def about(message: types.Message):
    text = (
        "🙋‍♂️ **Men haqimda:**\n\n"
        "• Ismim: **Jonibek**\n"
        "• Mutaxassislik: **Backend Developer**\n"
        "• Texnologiyalar: `Python`, `Django`, `Aiogram`, `PostgreSQL`, `JavaScript`\n\n"
        "Sizga sifatli va xavfsiz raqamli mahsulot yaratishda yordam beraman."
    )
    await message.answer(text, parse_mode="Markdown")

# --- 2. TAJRIBA ---
@router.message(F.text == "💼 Tajriba")
async def experience(message: types.Message):
    text = (
        "💼 **Ish tajribam:**\n\n"
        "🚀 **Junior Python Developer** | 2024 - Hozirgi vaqtda\n"
        "• Murakkab Telegram botlar va API tizimlarini ishlab chiqish.\n"
        "• Ma'lumotlar bazasini optimallashtirish.\n\n"
        "👨‍💻 **Middle Backend Developer** | 2024 - 2025\n"
        "• Django va FastAPI yordamida veb-servislar yaratish.\n"
        "• Jamoa bilan ishlash va kodni review qilish.\n\n"
        "🎓 **Freelance** | 2025 - 2026\n"
        "• 50 dan ortiq muvaffaqiyatli kichik va o'rta loyihalar."
    )
    await message.answer(text, parse_mode="Markdown")

# --- 3. XIZMATLAR ---
@router.message(F.text == "🧩 Xizmatlar")
async def services(message: types.Message):
    text = (
        "🧩 **Xizmatlar:**\n\n"
        "🤖 **Telegram Botlar** (E-commerce, CRM, Integratsiya)\n"
        "🌐 **Web Saytlar** (Backend tizimlar)\n"
        "⚙️ **API yaratish** (REST API)\n\n"
        "💰 Narxlar loyihaning murakkabligiga qarab kelishiladi."
    )
    await message.answer(text, parse_mode="Markdown")

# --- 4. ALOQA ---
@router.message(F.text == "📞 Aloqa")
async def contact_info(message: types.Message):
    text = (
        "📞 **Men bilan bog'lanish:**\n\n"
        "Savollaringiz yoki takliflaringiz bo'lsa, quyidagi platformalar orqali bog'lanishingiz mumkin.\n\n"
        "📍 **Manzil:** O'zbekiston, Samarqand\n"
        "📧 **Email:** `jurakulov_club@gmail..com`\n"
        "📞 **Tel:** `+998 90 93 145 32 23`\n\n"
        "*Tezkor javob olish uchun Telegram orqali yozishingizni tavsiya qilaman!*"
    )
    # Endi contact_inline() tepada import qilingani uchun xatosiz ishlaydi
    await message.answer(text, reply_markup=contact_inline(), parse_mode="Markdown")

# --- 5. LOYIHALAR ---
@router.message(F.text == "📁 Loyihalar")
async def projects(message: types.Message):
    await message.answer("📁 **Mening loyihalarim:**", reply_markup=get_projects_inline())

# --- INLINE CALLBACKLAR ---
@router.callback_query(F.data == "back_to_list")
async def back_list(call: types.CallbackQuery):
    await call.message.edit_text("📁 **Mening loyihalarim:**", reply_markup=get_projects_inline())

@router.callback_query(F.data.startswith("p_"))
async def show_project(call: types.CallbackQuery):
    if call.data == "p_shop":
        await call.message.edit_text(
            "🛍 **Online Do'kon Boti**\n\n"
            "• Savatcha tizimi\n• Click/Payme to'lovlari\n• Admin panel",
            reply_markup=project_links("https://github.com/example/shop")
        )
    elif call.data == "p_web":
        await call.message.edit_text(
            "🏥 **Klinika Tizimi**\n\n"
            "• Shifokorlar ro'yxati\n• Onlayn navbat\n• Bemorlar bazasi",
            reply_markup=project_links("https://github.com/example/clinic")
        )
    await call.answer()