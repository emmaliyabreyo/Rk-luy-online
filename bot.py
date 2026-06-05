import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. កំណត់ឱ្យប្រព័ន្ធបង្ហាញទិន្នន័យ (Logs) ក្នុង Render ងាយស្រួលមើលពេលមាន Error
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 2. ទាញយកលេខ Token និងលីង Web App ពីប្រព័ន្ធសុវត្ថិភាពរបស់ Render
# (អ្នកនឹងត្រូវទៅបំពេញលេខពិតប្រាកដនៅលើវេបសាយ Render ផ្ទាល់)
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """មុខងារឆ្លើយតបនៅពេលអ្នកប្រើប្រាស់ចុច /start"""
    user = update.effective_user
    
    # ពិនិត្យមើលថាតើបានបំពេញលីង WebApp រួចរាល់ហើយឬនៅ
    if not WEBAPP_URL:
        await update.message.reply_text("❌ ប្រព័ន្ធមិនទាន់បានកំណត់លីង Web App ទេ។ សូមទាក់ទងម្ចាស់បត។")
        return

    # បង្កើតប៊ូតុងសម្រាប់បើក Web App ផ្ទាល់ក្នុង Telegram
    keyboard = [
        [InlineKeyboardButton(text="🎮 បើក WebApp យកកូដ Roblox", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        f"សួស្តី {user.first_name}! 👋\n\n"
        f"សូមស្វាគមន៍មកកាន់ប្រព័ន្ធចែកកូដហ្គេម Roblox ឥតគិតថ្លៃ។\n"
        f"សូមចុចប៊ូតុង 'បើក WebApp' ខាងក្រោម ដើម្បីមើលពាណិជ្ជកម្ម ១៥វិនាទី និងដោះសោរកូដហ្គេមល្បីៗភ្លាមៗ! 🚀"
    )
    
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup)

def main():
    """មុខងារចម្បងសម្រាប់ដំណើរការបត"""
    if not BOT_TOKEN:
        print("❌ Error: មិនទាន់បានដាក់ BOT_TOKEN ក្នុង Environment Variables របស់ Render ទេ!")
        return

    print("🚀 បតតេឡេក្រាមចាប់ផ្តើមដំណើរការនៅលើ Render ហើយ...")
    
    # បង្កើតកម្មវិធីបត និងដាក់ឱ្យដំណើរការ (Polling)
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
