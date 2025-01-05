import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import start, check_job_scam, check_romance_scam, check_tech_support_scam, handle_message
from gemini_integration import configure_gemini
from utils import load_json

def main():
    TELEGRAM_TOKEN = "8151206204:AAFOqkLziQYuazHyL1GUZNcS_ekXw_r7OzQ"
    GEMINI_API_KEY = "AIzaSyBulnqflbB3SRzg4bR-wnG648jVACQGJ2g"

    gemini_model = configure_gemini(GEMINI_API_KEY)

    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.bot_data["gemini_model"] = gemini_model

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("checkJobScam", check_job_scam))
    application.add_handler(CommandHandler("checkRomanceScam", check_romance_scam))
    application.add_handler(CommandHandler("checkTechSupportScam", check_tech_support_scam))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()