import os
from pathlib import Path
from dotenv import load_dotenv

# Hozirgi config.py turgan papka yo'lini olish
BASE_DIR = Path(__file__).resolve().parent

# .env faylini aniq manzili bilan yuklash
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# --- DIAGNOSTIKA ---
if not TOKEN:
    print("❌ XATO: BOT_TOKEN o'qilmadi!")
    print(f"Hozirgi papka: {os.getcwd()}")
    print(f"Papkadagi fayllar: {os.listdir(BASE_DIR)}")
else:
    print(f"✅ Token muvaffaqiyatli yuklandi: {TOKEN[:5]}***")

if ADMIN_ID:
    ADMIN_ID = int(ADMIN_ID)