import os
import logging
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# កំណត់បង្ហាញ Logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

# --- 🟢 បង្កើត Web Server តូចមួយដើម្បីកុំឱ្យ Render បិទ (Exited early) ---
app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    # Render នឹងផ្តល់ Port ឱ្យតាមរយៈ os.getenv('PORT') ជាស្វ័យប្រវត្តិ
    port = int(os.getenv('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
# -------------------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not WEBAPP_URL:
        await update.message.reply_text("❌ មិនទាន់បានកំណត់លីង Web App ទេ។")
        return

    keyboard = [[InlineKeyboardButton(text="🎮 បើក WebApp យកកូដ Roblox", web_app=WebAppInfo(url=WEBAPP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_text = f"សួស្តី {user.first_name}! 👋\n\nសូមចុចប៊ូតុងខាងក្រោមដើម្បីបើក Web App មើលពាណិជ្ជកម្ម ១៥វិនាទី! 🚀"
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)

def main():
    if not BOT_TOKEN:
        print("❌ Error: មិនទាន់បានដាក់ BOT_TOKEN ទេ!")
        return

    # ដំណើរការ Web Server នៅក្នុង Thread ផ្សេងមួយទៀត
    threading.Thread(target=run_flask).start()

    print("🚀 បតតេឡេក្រាមចាប់ផ្តើមដំណើរការហើយ...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
