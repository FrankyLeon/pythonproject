from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import sys

# Define a command handler for the /start command
async def start(update: Update, context):
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}! Welcome to TryHarder's Test bot.")

# Define a message handler that echoes all received messages
async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

# Define the /stop command handler to stop the bot
async def stop(update: Update, context):
    await update.message.reply_text("Bot is shutting down. Goodbye!")
    print("Bot stopped", "\n")
    sys.exit(0)  # Terminate the script

# Main function to set up the bot
def main():
    TOKEN = '8179351807:AAFCb-hfm9j8pHweIGCUBecCem1loo96etg'  # Replace with your bot token
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers for /start and text messages
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('stop', stop))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until interrupted
    print("Bot is running...", "\n")
    app.run_polling()

if __name__ == '__main__':
    main()
