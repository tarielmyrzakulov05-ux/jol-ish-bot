import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 Найти смену", callback_data="find")],
        [InlineKeyboardButton("➕ Разместить смену", callback_data="job")],
        [InlineKeyboardButton("🌐 Наш сайт", callback_data="сайт")],
        [InlineKeyboardButton("ℹ️ О сервисе", callback_data="about")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Это JOL-Ish — сервис поиска сменной подработки в Бишкеке.\nВыбери, что хочешь сделать:",
        reply_markup=reply_markup
    )

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
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
