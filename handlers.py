from telegram import Update
from telegram.ext import ContextTypes
from session_manager import start_scam_check, get_session, update_session, end_session, check_session_timeout
from gemini_integration import classify_user_input
from utils import load_json

scam_responses = load_json("scam_responses.json")
scam_questions = load_json("scam_questions.json")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "🚨 *Welcome to the Scam Catcher Bot!* 🚨\n\n"
        "I can help you identify and avoid scams, and provide advice if you’ve been scammed.\n\n"
        "📋 *How to use me:*\n"
        "1. Use /checkJobScam to check if a job offer is a scam.\n"
        "2. Use /checkRomanceScam to check if a romance situation is a scam.\n"
        "3. Use /checkTechSupportScam to check if a tech support request is a scam.\n\n"
        "Let's stay safe together! 🛡️"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

async def check_job_scam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    start_scam_check(user_id, "job_scam")
    await ask_next_question(update, context, user_id)

async def check_romance_scam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    start_scam_check(user_id, "romance_scam")
    await ask_next_question(update, context, user_id)

async def check_tech_support_scam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    start_scam_check(user_id, "tech_support_scam")
    await ask_next_question(update, context, user_id)

async def ask_next_question(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id: int):
    session = get_session(user_id)
    if session:
        scam_type = session["scam_type"]
        question_index = session["question_index"]
        if question_index < len(scam_questions[scam_type]["questions"]):
            question = scam_questions[scam_type]["questions"][question_index]
            await update.message.reply_text(question)
        else:
            await evaluate_scam(update, context, user_id)

async def evaluate_scam(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id: int):
    session = get_session(user_id)
    if session:
        scam_type = session["scam_type"]
        responses = session["responses"]
        questions = scam_questions[scam_type]["questions"]

        # Sync questions and responses into a dictionary
        qa_pairs = {questions[i]: responses[i] for i in range(len(questions))}

        # Prepare the prompt for the Gemini model
        prompt = (
            "You are a secret agent detective specializing in identifying scams. "
            "Based on the following questions and answers, determine if this is a scam or not. "
            "Provide a detailed analysis and conclusion.\n\n"
            "Questions and Answers:\n"
        )
        for question, answer in qa_pairs.items():
            prompt += f"- **Question:** {question}\n  **Answer:** {answer}\n"

        prompt += (
            "\nAnalysis:\n"
            "1. Identify any red flags or suspicious patterns in the answers.\n"
            "2. Compare the situation with known scam tactics.\n"
            "3. Provide a conclusion on whether this is likely a scam or not.\n\n"
            "Conclusion:"
        )

        # Get the evaluation from the Gemini model
        gemini_model = context.bot_data["gemini_model"]
        evaluation = gemini_model.generate_content(prompt).text
        print('evaluations = \n\n\n\n',evaluation)

        # Send the evaluation to the user
        await update.message.reply_text(evaluation)

        # End the session
        end_session(user_id)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_input = update.message.text

    if check_session_timeout(user_id):
        await update.message.reply_text("Your session has timed out. Please start a new scam check if needed.")
        return

    session = get_session(user_id)
    if session:
        update_session(user_id, user_input)
        await ask_next_question(update, context, user_id)
    else:
        concern = classify_user_input(context.bot_data["gemini_model"], user_input)
        if concern in scam_responses:
            response = scam_responses[concern]["response"]
        else:
            response = "I’m here to help you with scam-related concerns. Please use /checkJobScam, /checkRomanceScam, or /checkTechSupportScam to start a scam check."
        await update.message.reply_text(response, parse_mode="Markdown")