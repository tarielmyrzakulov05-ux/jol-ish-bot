import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name

    keyboard = [
        [InlineKeyboardButton("🔍 Найти смену", callback_data="find")],
        [InlineKeyboardButton("➕ Разместить смену", callback_data="job")],
        [InlineKeyboardButton("💬 Чат", callback_data="chat")],
        [InlineKeyboardButton("🌐 Наш сайт", callback_data="site")],
        [
            InlineKeyboardButton("🇰🇬 Кыргызча", callback_data="kg"),
            InlineKeyboardButton("🇬🇧 English", callback_data="en")
        ],
        [InlineKeyboardButton("🎙️ Голосовой помощник", callback_data="voice")],
        [InlineKeyboardButton("ℹ️ О сервисе", callback_data="about")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"Привет, {name}! 👋\n\n"
        "Это JOL-Ish — сервис поиска сменной подработки в Бишкеке.\n\n"
        "Выбери, что хочешь сделать:",
        reply_markup=reply_markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 JOL-Ish\n\n"
        "/start — открыть главное меню\n"
        "/help — показать справку\n\n"
        "Ты можешь найти смену, разместить вакансию, "
        "перейти на сайт, выбрать язык или воспользоваться голосовым помощником."
    )


async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙂 Я пока не совсем понял сообщение.\n\n"
        "Напиши /start, чтобы открыть главное меню."
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "find":
        await query.message.reply_text(
            "🔍 Чтобы найти смену, заполни форму:\n\n"
            "https://docs.google.com/forms/d/e/1FAIpQLScwh1D5UKB2aCvkP4RikWPxGetB_JwO2_FnALGe5_IyimIubg/viewform"
        )

    elif query.data == "job":
        await query.message.reply_text(
            "➕ Чтобы разместить смену, заполни форму:\n\n"
            "https://docs.google.com/forms/d/e/1FAIpQLSey3k8gent4eHEceU4CszmDj2SNr6UKKH7UqQPwiN2xlEyqkg/viewform"
        )

    elif query.data == "site":
        await query.message.reply_text(
            "🌐 Заходи на наш сайт:\n\n"
            "https://jol-ish-connect.lovable.app"
        )

    elif query.data == "chat":
        await query.message.reply_text(
            "💬 Чат JOL-Ish\n\n"
            "Напиши мне свой вопрос, например:\n"
            "• Где найти смену?\n"
            "• Как разместить вакансию?\n"
            "• Как работает JOL-Ish?\n\n"
            "Я постараюсь помочь 🙂"
        )

    elif query.data == "kg":
        await query.message.reply_text(
            "🇰🇬 Кыргызча режим\n\n"
            "JOL-Ish — Бишкекте сменалык жумуш табууга жардам берген сервис.\n\n"
            "Сменаны табуу же вакансия жайгаштыруу үчүн башкы менюну ачыңыз: /start"
        )

    elif query.data == "en":
        await query.message.reply_text(
            "🇬🇧 English mode\n\n"
            "JOL-Ish helps people find shift-based part-time jobs in Bishkek.\n\n"
            "To find a shift or post a vacancy, open the main menu: /start"
        )

    elif query.data == "voice":
        await query.message.reply_text(
            "🎙️ Голосовой помощник\n\n"
            "Отправь мне голосовое сообщение, и я постараюсь его распознать."
        )

    elif query.data == "about":
        await query.message.reply_text(
            "ℹ️ JOL-Ish — сервис поиска сменной подработки в Бишкеке.\n\n"
            "Найди подходящую смену или размести вакансию.\n\n"
            "Подробнее:\n"
            "https://sites.google.com/view/jol-ish-bishkek"
        )


async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎙️ Голосовое сообщение получено!\n\n"
        "Сейчас голосовой помощник обрабатывает сообщение."
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

app.add_handler(CallbackQueryHandler(button_handler))

app.add_handler(
    MessageHandler(filters.VOICE, voice_handler)
)

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text)
)

app.run_polling()
