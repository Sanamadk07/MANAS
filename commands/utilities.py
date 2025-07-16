import datetime
import pyautogui
import pyjokes
from core.tts import speak

def handle_utilities(command):
    if 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}.")
        return True

    elif 'date' in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}.")
        return True

    elif 'screenshot' in command:
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        speak("Screenshot taken and saved as screenshot.png")
        return True

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        speak(joke)
        return True

    return False
