from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Hello! I am here to help you with troubleshooting.")

if __name__ == '__main__':
    token = '8974308335:AAGjrvc8avO9nFzIMLyP-mNwQjXudGtDiKI'
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()
