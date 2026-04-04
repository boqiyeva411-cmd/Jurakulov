from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_projects_inline():
    buttons = [
        [InlineKeyboardButton(text="🛍 Online Do'kon (Bot)", callback_data="p_shop")],
        [InlineKeyboardButton(text="🏥 Klinika Tizimi (Web)", callback_data="p_web")],
        [InlineKeyboardButton(text="📊 Ma'lumotlar Tahlili", callback_data="p_data")],
        [InlineKeyboardButton(text="🌐 Shaxsiy Saytim", url="https://portfolio.uz")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def project_links(github_url):
    buttons = [
        [InlineKeyboardButton(text="💻 Kodni ko'rish (GitHub)", url=github_url)],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_list")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
def contact_inline():
    buttons = [
        [
            InlineKeyboardButton(text="💬 Telegram (Shaxsiy)", url="https://t.me/Jurakulov_off1"),
            InlineKeyboardButton(text="📸 Instagram", url="https://instagram.com/SIZNING_PROFIL")
        ],
        [
            InlineKeyboardButton(text="📧 LinkedIn", url="https://linkedin.com/in/SIZNING_PROFIL"),
            InlineKeyboardButton(text="🖥 GitHub", url="https://github.com/SIZNING_PROFIL")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)