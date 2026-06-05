

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# 🛠️ កន្លែងត្រូវផ្លាស់ប្តូរទិន្នន័យរបស់អ្នក
BOT_TOKEN = "8003134460:AAFr-D_fGIyj0Sev2G3lFsJ2kmtUkQ9FMLo" # ដាក់ Token របស់បតអ្នក
WEBAPP_URL = "rk-luy-online-tjjl.vercel.app" # ដាក់លីងវេបសាយ HTTPS ដែលបានមកពីវគ្គទី៤

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    # បង្កើតប៊ូតុងប្រភេទ WebApp (បើកផ្ទាល់ក្នុងតេឡេក្រាម)
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
    print("Bot កំពុងដំណើរការហើយ...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
