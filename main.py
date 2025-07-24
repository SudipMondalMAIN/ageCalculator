from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! Send your birthdate like this: /age YYYY-MM-DD")

# /age command handler
async def calculate_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        birth_date_str = context.args[0]
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )
        await update.message.reply_text(f"📅 Your age is: {age} years")
    except (IndexError, ValueError):
        await update.message.reply_text("❌ Please use the correct format: /age YYYY-MM-DD")

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("7398657418:AAFQW0gn9ks-IooneZVUtpkgg7HHYmjouKQ").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("age", calculate_age))

    print("🤖 Bot is running...")
    app.run_polling()
