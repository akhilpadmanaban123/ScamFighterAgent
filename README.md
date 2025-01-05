
**📝 ScamFighterAgent: Your Intelligent Scam-Busting Companion**

**🛡️ Protect Yourself from Online Deception**

ScamFighterAgent is a powerful Telegram bot designed to empower you in the fight against online scams. It leverages cutting-edge technology and user-friendly interaction to help you identify and avoid deceptive tactics.

**🎯 Key Features:**

- **Scam Detection:** Unmask potential scams with ease. Initiate checks using commands like `/checkJobScam`, `/checkRomanceScam`, or `/checkTechSupportScam`.
- **Interactive Sessions:** Engage in a guided conversation with the bot, providing details about the suspected scam.
- **Predefined Responses:** Access a wealth of knowledge through the `scam_responses.json` file, offering tailored advice for common scam scenarios.
- **Gemini LLM Integration:** Harness the power of the Gemini Large Language Model (LLM) for in-depth analysis and scam evaluation.
- **User-Friendly Interface:** Enjoy clear and visually appealing responses enhanced by Markdown formatting and emojis.

**🏗️ Project Structure:**

```
ScamFighterAgent/
├── bot.py        # Main bot script initialization and execution
├── handlers.py    # Telegram command and message handlers
├── session_manager.py  # Manages user sessions during scam checks
├── gemini_integration.py  # Handles Gemini LLM interaction
├── utils.py       # Utility functions (e.g., JSON loading)
├── scam_responses.json  # Predefined responses for scam concerns
└── scam_questions.json  # Questions and conditions for scam checks
```

**🧭 File Descriptions:**

1. **bot.py:** The heart of the bot, coordinating Telegram integration, handler management, and Gemini LLM interaction for scam detection.
2. **handlers.py:** Handles user interactions through Telegram commands and messages, guiding scam checks and utilizing the Gemini LLM.
3. **session_manager.py:** Tracks user responses, session start times, and timeouts, ensuring smooth session management.
4. **gemini_integration.py:** Facilitates communication with the Gemini LLM, sending user input for analysis and receiving scam evaluations.
5. **utils.py:** Provides essential utility functions, such as loading JSON files for responses and questions.
6. **scam_responses.json:** Stores pre-defined responses addressing common scam concerns, providing immediate guidance to users.
7. **scam_questions.json:** Houses the questions and conditions used during different types of scam checks, tailoring the interaction for specific scenarios.

**🕵️ How It Works:**

1. **User Interaction:** Initiate a scam check using a relevant command (e.g., `/checkJobScam`).
2. **Session Management:** The bot establishes a session to track your interaction, ensuring a seamless experience. The session automatically times out after 20 minutes of inactivity.
3. **Scam Evaluation:** The bot guides you through a series of questions tailored to the suspected scam type.
4. **Gemini LLM Analysis:** Once you've provided all responses, the bot sends the collected data to the Gemini LLM for expert analysis.
5. **Response to User:** The bot delivers the Gemini LLM's comprehensive evaluation in a clear and user-friendly format.

**📈 Example Workflow:**

**User:** `/checkJobScam`

**Bot:** "Can you describe the job offer? (e.g., part-time job earning $1000/day)"

**User:** "They said I can earn $2000/day by reviewing pages."

**Bot:** "Are they asking you to pay any upfront fees?"

**User:** "No."

**Bot:** "Are they promising unrealistic earnings for minimal work?"

**User:** "Yes."

**Bot:** "Are they asking you to review pages or like Instagram posts for payment?"

**User:** "Yes."

**Bot:** "Are they asking for your personal or financial information?"

**User:** "Yes."

**Bot:** "Based on your responses, this is likely a scam. Avoid sharing any personal or financial information and report the offer to the relevant authorities."

**🚀 Next Steps (Version 2.0):**

- **Enhanced Analysis:** Deepen the Gemini LLM's capabilities by incorporating more intricate scam patterns and red flags.
- **Expanded Coverage:** Support additional scam types (e.g., investment, phishing) to provide broader protection.
- **User Feedback:** Integrate user feedback mechanisms to refine the bot's accuracy based on real-world encounters.
- **Database Integration:** Store user interactions and scam reports for future analysis and improvement.
- **Multilingual Support:** Break language barriers by providing support for multiple languages,
