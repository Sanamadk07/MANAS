import google.generativeai as genai
from core.tts import speak

genai.configure(api_key="AIzaSyCRw38ai8-QF85gomBFgKIvTFAzRjzEOhI")  # Replace with actual key
model = genai.GenerativeModel('gemini-1.5-flash')

def ask_gemini(prompt):
    import google.generativeai as genai
    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        convo = model.start_chat()
        convo.send_message(prompt)
        response = convo.last.text.strip()
        speak(response)
        return response
    except Exception as e:
        speak("Sorry, I couldn't answer that.")
        print("Gemini error:", e)
        return None
