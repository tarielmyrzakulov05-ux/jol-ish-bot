import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton("🔍 Найти смену", callback_data="find")],
        [InlineKeyboardButton("➕ Разместить смену", callback_data="job")],
        [InlineKeyboardButton("🌐 Наш сайт", callback_data="сайт")],
        [InlineKeyboardButton("ℹ️ О сервисе", callback_data="about")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Привет, {name}! Это JOL-Ish — сервис поиска сменной подработки в Бишкеке.\nВыбери, что хочешь сделать:",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вот что я умею:\n\n"
        "/start — открыть главное меню\n"
        "/help — показать эту справку\n\n"
        "В главном меню можно найти смену, разместить вакансию, перейти на сайт или узнать больше о сервисе."
    )

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Не совсем понял 🙂 Напиши /start, чтобы открыть меню, или /help для справки.")

async def button_handler(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == "find":
        await query.message.reply_text("Чтобы найти смену, заполни форму:\nhttps://docs.google.com/forms/d/e/1FAIpQLScwh1D5UKB2aCvkP4RikWPxGetB_JwO2_FnALGe5_IyimIubg/viewform")
    elif query.data == "job":
        await query.message.reply_text("Чтобы разместить смену, заполни форму:\nhttps://docs.google.com/forms/d/e/1FAIpQLSey3k8gent4eHEceU4CszmDj2SNr6UKKH7UqQPwiN2xlEyqkg/viewform")
    elif query.data == "сайт":
        await query.message.reply_text("Заходи на наш сайт — там удобный подбор смен с процентом совпадения:\nhttps://jol-ish-connect.lovable.app")
    elif query.data == "about":
        await query.message.reply_text("JOL-Ish — сервис поиска сменной подработки в Бишкеке. Найди подходящую смену или размести вакансию.\n\nПодробнее на сайте:\nhttps://sites.google.com/view/jol-ish-bishkek")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))
app.run_polling()
