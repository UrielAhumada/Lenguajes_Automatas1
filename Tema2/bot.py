import logging
import re
import datetime

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresiones regulares
expresion_saludo = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
expresion_estado = re.compile(r"(?:¿)?c[oó]mo est[aá]s\??", re.IGNORECASE)
expresion_hora = re.compile(r"dame la hora", re.IGNORECASE)
expresion_operacion = re.compile(r"cu[aá]nto es (\d+)\s*\+\s*(\d+)", re.IGNORECASE)
expresion_cantante_favorito = re.compile(r"cual es mi cantante favorito", re.IGNORECASE)
expresion_estoy_bien = re.compile(r"estoy bien", re.IGNORECASE)
expresion_estoy_mal = re.compile(r"estoy mal", re.IGNORECASE)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches any regular expression."""
    message_text = update.message.text
    if expresion_saludo.search(message_text):
        await update.message.reply_text("¡Hola! ¿Cómo estás?")
    elif expresion_estado.search(message_text):
        await update.message.reply_text("Estoy bien, gracias por preguntar.")
    elif expresion_hora.search(message_text):
        now = datetime.datetime.now()
        await update.message.reply_text(f"La hora actual es: {now.strftime('%H:%M:%S')}")
    elif expresion_operacion.search(message_text):
        match = expresion_operacion.search(message_text)
        resultado = int(match.group(1)) + int(match.group(2))
        await update.message.reply_text(f"El resultado de la suma es: {resultado}")
    elif expresion_cantante_favorito.search(message_text):
        await update.message.reply_text("Tu artista favorito es The Weeknd.")
    elif expresion_estoy_bien.search(message_text):
        await update.message.reply_text("Me alegro.")
    elif expresion_estoy_mal.search(message_text):
        await update.message.reply_text("Lo siento, espero que te sientas mejor pronto.")
    else:
        await update.message.reply_text("No entendí tu mensaje.")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("6887875712:AAHEp62OFT5YMzZePGM2KIRGTM7TcCgAIWU").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()