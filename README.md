# ScamFighterAgent
Scam Fighter Agent (Version 1.0)

Project Description
The Scam Fighter Agent is a Telegram bot designed to help users identify and avoid scams. It provides tailored advice for various scam scenarios (e.g., job scams, romance scams, tech support scams) and helps users determine if a situation they are encountering is likely a scam. The bot uses a combination of predefined responses, user interaction, and the Gemini LLM for intelligent analysis.

Key Features
Scam Detection:

Users can start a scam-checking session using commands like /checkJobScam, /checkRomanceScam, or /checkTechSupportScam.

The bot asks a series of questions to gather information about the situation.

Based on the user's responses, the bot evaluates whether the situation is likely a scam.

Predefined Responses:

The bot uses a JSON file (scam_responses.json) to provide tailored advice for common scam-related concerns (e.g., "I paid money to scammers," "How to avoid scams in the future").

Interactive Sessions:

The bot maintains a session for each user during a scam check.

Sessions time out after 20 minutes of inactivity.

Gemini LLM Integration:

The bot uses the Gemini LLM to classify user inputs and evaluate scam scenarios.

The model acts as a "secret agent detective" to analyze user responses and provide detailed conclusions.

User-Friendly Interface:

The bot uses Markdown formatting and emojis to make responses visually appealing and easy to read.

Project Structure
Copy
ScamFighterAgent/
├── bot.py                  # Main bot script
├── handlers.py             # Handlers for commands and messages
├── session_manager.py      # Session management for scam checks
├── gemini_integration.py   # Gemini LLM integration
├── utils.py                # Utility functions (e.g., JSON loading)
├── scam_responses.json     # Predefined responses for scam-related concerns
└── scam_questions.json     # Questions and conditions for scam checks
File Descriptions
1. bot.py
The main script that initializes and runs the bot.

Sets up the Telegram bot application and adds handlers for commands and messages.

Integrates the Gemini LLM for scam detection and analysis.

2. handlers.py
Contains handlers for Telegram commands (/start, /checkJobScam, etc.) and messages.

Manages user interactions during scam-checking sessions.

Calls the Gemini LLM for classifying user inputs and evaluating scam scenarios.

3. session_manager.py
Manages active sessions for scam checks.

Tracks user responses, session start time, and session timeout.

Ends sessions after 20 minutes of inactivity.

4. gemini_integration.py
Handles integration with the Gemini LLM.

Provides functions for classifying user inputs and generating detailed scam evaluations.

5. utils.py
Contains utility functions, such as loading JSON files.

6. scam_responses.json
Stores predefined responses for common scam-related concerns.

7. scam_questions.json
Stores questions and conditions for different types of scams.

How It Works
User Interaction:

The user starts a scam-checking session using a command (e.g., /checkJobScam).

The bot asks a series of questions based on the type of scam being checked.

Session Management:

The bot tracks the user's responses and maintains a session for 20 minutes.

If the user is inactive for 20 minutes, the session ends automatically.

Scam Evaluation:

After collecting all responses, the bot syncs the questions and answers into a dictionary.

The bot sends the data to the Gemini LLM for analysis.

The model evaluates the situation and provides a detailed conclusion.

Response to User:

The bot sends the evaluation to the user in a structured and user-friendly format.

Example Workflow
User: /checkJobScam

Bot: "Can you describe the job offer? (e.g., part-time job earning $1000/day)"

User: "They said I can earn $2000/day by reviewing pages."

Bot: "Are they asking you to pay any upfront fees?"

User: "No."

Bot: "Are they promising unrealistic earnings for minimal work?"

User: "Yes."

Bot: "Are they asking you to review pages or like Instagram posts for payment?"

User: "Yes."

Bot: "Are they asking for your personal or financial information?"

User: "Yes."

Bot: "Based on your responses, this is likely a scam. Avoid sharing any personal or financial information and report the offer to the relevant authorities."

Next Steps (Version 2.0)
Deep Analysis:

Enhance the Gemini LLM's analysis by incorporating more detailed scam patterns and red flags.

Add support for additional scam types (e.g., investment scams, phishing scams).

User Feedback:

Allow users to provide feedback on the bot's evaluation to improve accuracy.

Database Integration:

Store user interactions and scam reports in a database for future analysis and improvement.

Multilingual Support:

Add support for multiple languages to reach a wider audience.

Advanced Session Management:

Allow users to resume interrupted sessions.

Add a command to manually end a session.


