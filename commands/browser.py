# commands/browser.py

import os
import webbrowser
import pyautogui
import time
from core.tts import speak

def open_chrome_and_search(query):
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    if os.path.exists(chrome_path):
        speak("Opening Chrome browser.")
        os.startfile(chrome_path)
        time.sleep(5)  # wait for browser to open
        if query:
            pyautogui.write(query, interval=0.1)
            pyautogui.press('enter')
        else:
            speak("Chrome is opened.")
    else:
        speak("Chrome is not installed.")

def handle_browser(command):
    if 'open chrome' in command:
        open_chrome_and_search("")
        return True

    elif 'search google' in command:
        speak("What should I search for?")
        from core.listener import take_command
        query = take_command()
        open_chrome_and_search(query)
        return True

    elif 'search youtube' in command:
        speak("What should I search on YouTube?")
        from core.listener import take_command
        query = take_command()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        speak(f"Searching YouTube for {query}.")
        return True

    return False
