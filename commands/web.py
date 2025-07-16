import webbrowser
from core.tts import speak
from core.listener import take_command

def handle_web(command):
    if 'search google' in command:
        speak("What should I search for?")
        query = take_command()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching Google for {query}.")
        return True

    elif 'search youtube' in command:
        speak("What should I search on YouTube?")
        query = take_command()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        speak(f"Searching YouTube for {query}.")
        return True

    elif 'open facebook' in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
        return True

    elif 'open instagram' in command or 'open insta' in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")
        return True

    elif 'open messenger' in command:
        webbrowser.open("https://www.messenger.com")
        speak("Opening Messenger.")
        return True

    return False