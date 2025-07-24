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
        if birth_date > today:
            await update.message.reply_text("❌ Birthdate cannot be in the future!")
            return

        # Calculate years, months, days
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            previous_month = today.month - 1 if today.month > 1 else 12
            previous_year = today.year if today.month > 1 else today.year - 1
            days_in_prev_month = (datetime(previous_year, previous_month + 1, 1) - datetime(previous_year, previous_month, 1)).days
            days += days_in_prev_month

        if months < 0:
            years -= 1
            months += 12

        await update.message.reply_text(f"📅 Your age is: {years} years, {months} months, {days} days")
    except (IndexError, ValueError):
        await update.message.reply_text("❌ Please use the correct format: /age YYYY-MM-DD")

# Run the bot
if __name__ == '__main__':
    import os
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7398657418:AAFQW0gn9ks-IooneZVUtpkgg7HHYmjouKQ")  # Replace with your env var or other secure method
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("age", calculate_age))

    print("🤖 Bot is running...")
    app.run_polling()
