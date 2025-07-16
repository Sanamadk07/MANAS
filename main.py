# main.py

from core.listener import take_command
from core.tts import speak, speak_nepali
from core.ai import ask_gemini
from core.ai import ask_gemini_with_timeout

from commands.utilities import handle_utilities
from commands.apps import handle_apps
from commands.system import handle_system
from commands.web import handle_web
from commands.browser import handle_browser
from commands.files import handle_files

def wish_user():
    speak_nepali("नमस्ते, म मनस हुँ। म तपाईंलाई कसरी सहयोग गर्न सक्छु?")
    speak("MANAS is now online. How may I help you?")

def run_samdhi():
    wish_user()
    while True:
        command = take_command()

        if not command:
            continue

        # Try handling the command in each module
        handled = (
            handle_utilities(command) or
            handle_apps(command) or
            handle_system(command) or
            handle_web(command) or
            handle_browser(command) or
            handle_files(command)
        )

        if handled:
            # If user said exit or bye, close the assistant gracefully
            if 'exit' in command or 'bye' in command:
                speak("Goodbye! Have a nice day.")
                break
            continue

        # If no module handled the command, query AI
        speak("Let me think...")
        ask_gemini_with_timeout(command)

if __name__ == "__main__":
    run_samdhi()
