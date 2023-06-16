#esempio_bot_telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print(TOKEN)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello_funct))
    app.add_handler(CommandHandler("waddup", waddup_funct))
    app.add_handler(CommandHandler("smile", smile_funct))
    app.run_polling()

async def hello_funct(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    hello_var = update.effective_user.first_name
    await update.message.reply_text("Hello %s" % hello_var)

async def waddup_funct(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    waddup_var = update.effective_user.first_name
    await update.message.reply_text("Waddup %s, fr no cap" % waddup_var)

async def smile_funct(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(":)")

if __name__ == '__main__':
    main()
    
