import os
from core.tts import speak

def handle_apps(command):
    if 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")
        return True

    elif 'open chrome' in command:
        path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(path):
            speak("Opening Chrome")
            os.startfile(path)
        else:
            speak("Chrome is not installed at the default location.")
        return True

    elif 'open vs code' in command or 'open code' in command:
        path = "C:\\Users\\YourUserName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        if os.path.exists(path):
            speak("Opening Visual Studio Code")
            os.startfile(path)
        else:
            speak("VS Code not found.")
        return True

    return False