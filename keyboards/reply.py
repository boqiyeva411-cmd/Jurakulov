from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = [
        [KeyboardButton(text="🙋‍♂️ Men haqimda"), KeyboardButton(text="💼 Tajriba")],
        [KeyboardButton(text="🧩 Xizmatlar"), KeyboardButton(text="📁 Loyihalar")],
        [KeyboardButton(text="📞 Aloqa"), KeyboardButton(text="📝 Murojaat")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Bo'limni tanlang...")

def phone_kb():
    kb = [[KeyboardButton(text="📱 Raqamni yuborish", request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)