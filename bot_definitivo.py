#bot_definitivo
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sqlite3

db = sqlite3.connect("./dae_somma.db")

with open("token.txt", "r") as f:
    TOKEN = f.read()
    print(TOKEN)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello_funct))
    app.add_handler(CommandHandler("waddup", waddup_funct))
    app.add_handler(CommandHandler("smile", smile_funct))
    app.add_handler(CommandHandler("dae", get_dae))

    app.run_polling()

async def hello_funct(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    hello_var = update.effective_user.first_name
    await update.message.reply_text("Hello %s" % hello_var)

async def waddup_funct(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    waddup_var = update.effective_user.first_name
    await update.message.reply_text("Waddup %s, fr no cap" % waddup_var)

async def smile_funct(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(":)")

async def get_dae(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cursor = db.cursor()
    query = "SELECT struttura FROM dispositivi"
    cursor.execute(query)
    rows = cursor.fetchall()

    result_list = [r[0] for r in rows] #usando la posizione 0 seleziono solo il primo elemento
    message = ' '.join(result_list) #la join prende tutti gli elementi e li unisce in una stringa
    await update.message.reply_text(message)

if __name__ == '__main__':
    main()
    
