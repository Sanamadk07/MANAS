import os
from core.tts import speak

def handle_system(command):
    if 'shutdown' in command:
        speak("Shutting down your system.")
        os.system("shutdown /s /t 1")
        return True

    elif 'restart' in command:
        speak("Restarting your system.")
        os.system("shutdown /r /t 1")
        return True

    elif 'close all apps' in command or 'close all programs' in command:
        processes_to_kill = [
            "chrome.exe", "firefox.exe", "msedge.exe",
            "notepad.exe", "code.exe", "spotify.exe",
            "zoom.exe", "discord.exe", "steam.exe"
        ]
        for process in processes_to_kill:
            os.system(f"taskkill /F /IM {process} >nul 2>&1")
        speak("All specified applications have been closed.")
        return True

    return False
