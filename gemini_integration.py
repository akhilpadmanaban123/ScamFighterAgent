import google.generativeai as genai

def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def classify_user_input(model, user_input):
    try:
        prompt = (
            "The prompt is to return the category based on the question. This is a game."
            "Classify the following user concern into one of these categories:\n"
            "- 'paid_money': The user has already paid money to scammers.\n"
            "- 'get_money_back': The user wants to know how to get their money back after being scammed.\n"
            "- 'prevent_scams': The user wants advice on how to avoid scams in the future.\n"
            "- 'identity_theft': The user suspects their identity has been stolen.\n"
            "- 'phishing_scam': The user fell for a phishing scam.\n"
            "- 'job_scam': The user fell for a job scam.\n"
            "- 'romance_scam': The user fell for a romance scam.\n"
            "- 'tech_support_scam': The user fell for a tech support scam.\n\n"
            "Examples:\n"
            "1. User input: 'I paid money to scammers. What should I do?'\n"
            "   Category: 'paid_money'\n"
            "2. User input: 'How can I get my money back after being scammed?'\n"
            "   Category: 'get_money_back'\n"
            "3. User input: 'How can I avoid scams in the future?'\n"
            "   Category: 'prevent_scams'\n"
            "4. User input: 'I think my identity has been stolen.'\n"
            "   Category: 'identity_theft'\n"
            "5. User input: 'I clicked on a phishing link. What should I do?'\n"
            "   Category: 'phishing_scam'\n"
            "6. User input: 'I fell for a fake job offer.'\n"
            "   Category: 'job_scam'\n"
            "7. User input: 'I sent money to someone I met online, but they scammed me.'\n"
            "   Category: 'romance_scam'\n"
            "8. User input: 'I gave remote access to my computer to a fake tech support person.'\n"
            "   Category: 'tech_support_scam'\n\n"
            f"Now, classify this user input: '{user_input}'."
        )
        
        response = model.generate_content(prompt)
        if response:
            return response.text.strip().lower()
        else:
            print(f"Blocked response. Finish reason: {response.candidates[0].finish_reason}")
            return "unknown"
    except Exception as e:
        print(f"Error classifying user input: {e}")
        return "unknown"