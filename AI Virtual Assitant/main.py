import speech_recognition as sr
import subprocess
import datetime
import pywhatkit
import webbrowser

recognizer = sr.Recognizer()

# macOS built-in “say” command for natural voice
def talk(text):
    print(f"🧠 Alexa says: {text}")
    subprocess.call(["say", "-v", "Samantha", text])

def listen_for_command():
    """Listen for user's speech and return text"""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=5)
    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print(f"🗣 You said: {command}")
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        talk("Sorry, I can't reach Google right now.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

def handle_command(command):
    """Respond to known commands"""
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The time is {time}")

    elif 'open youtube' in command or 'youtube' in command:
        talk("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command.startswith('play '):
        song = command.replace('play ', '')
        talk(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif 'who is' in command or 'what is' in command:
        talk(f"Searching {command}")
        pywhatkit.search(command)

    elif 'stop' in command or 'exit' in command or 'quit' in command:
        talk("Goodbye!")
        exit()

    else:
        talk("Sorry, I didn't catch that.")

def main():
    talk("Hi , how can I help you today?")
    while True:
        command = listen_for_command()
        if command.startswith("alexa"):
            command = command.replace("alexa", "", 1).strip()
            if command:
                handle_command(command)
        # if the user doesn't say "alexa", it ignores it

if __name__ == "__main__":
    main()
