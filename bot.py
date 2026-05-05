from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = " 8680295785:AAGXGqxVIpYz3nU1Sa87s3561sAzvHtNARs"

# Welcome Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Welcome to 5% Brothers Ludo Group 🔥")

# New Member Welcome
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"Welcome {member.first_name} bhai 🎉\nGame k liye ready ho jao 🔥")

# Auto Reply System
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "hi" in text or "hello" in text:
        await update.message.reply_text("Hello bhai 🙂 Welcome!")

    elif "payment" in text or "qr" in text:
        await update.message.reply_text("💰 Payment ke liye yeh QR use kare:\n[ https://t.me/cwwsDUksqTAwOWQ1 ]")

    elif "join" in text:
        await update.message.reply_text("Group join karne ke liye admin se contact kare 👍")

# Admin Command
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 Rules:\n1. Respect sabka\n2. No spam\n3. Fair play only")

# Anti-Spam (basic)
async def spam_filter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "http" in text or "https" in text:
        await update.message.delete()

app = ApplicationBuilder().token(TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("rules", rules))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.add_handler(MessageHandler(filters.TEXT, spam_filter))

print("Bot is running...")
app.run_polling()