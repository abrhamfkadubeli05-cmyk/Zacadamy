from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Hello! I am here to help you with troubleshooting.")

if __name__ == '__main__':
    token = 'YOUR_BOT_TOKEN_HERE'
    application = ApplicationBuilder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()
