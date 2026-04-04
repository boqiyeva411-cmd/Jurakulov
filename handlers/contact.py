from aiogram import Router, F, types, Bot
from aiogram.fsm.context import FSMContext
from states.states import Form
from keyboards.reply import phone_kb, main_menu
from config import ADMIN_ID

router = Router()

@router.message(F.text == "📝 Murojaat")
async def start_contact(message: types.Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer("✍️ Ismingizni kiriting:", reply_markup=types.ReplyKeyboardRemove())

@router.message(Form.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.phone)
    await message.answer("📞 Telefon raqamingizni yuboring:", reply_markup=phone_kb())

@router.message(Form.phone, F.contact)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(Form.message)
    await message.answer("💬 Xabaringizni yozing:")

@router.message(Form.message)
async def get_msg(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    
    # Adminga yuborish
    admin_text = (
        "🔔 **Yangi Murojaat!**\n\n"
        f"👤 Ism: {data['name']}\n"
        f"📞 Tel: {data['phone']}\n"
        f"💬 Xabar: {message.text}\n"
        f"🔗 Profil: [Link](tg://user?id={message.from_user.id})"
    )
    await bot.send_message(ADMIN_ID, admin_text, parse_mode="Markdown")
    
    await state.clear()
    await message.answer("🚀 Rahmat! Xabaringiz adminga yuborildi.", reply_markup=main_menu())