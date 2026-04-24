import speech_recognition as sr
import webbrowser
import pyttsx3

# 🔊 Voice setup (Windows)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

recognizer = sr.Recognizer()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()

    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    elif "stackoverflow" in command:
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")

    elif "reddit" in command:
        speak("Opening Reddit")
        webbrowser.open("https://www.reddit.com")

    elif "netflix" in command:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")

    elif "spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")

    elif "amazon" in command:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")

    elif "gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "exit" in command:
        speak("Goodbye bhai")
        exit()

    else:
        speak("Command not recognized")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    wake_words = ["jarvis", "hey jarvis", "hi jarvis"]

    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)

                print("You said:", command)

                # 🔥 Wake word
                if any(word in command.lower() for word in wake_words):
                    speak("Yes")

                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        print("Jarvis Active...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)

                        print("Command:", command)
                        processCommand(command)

                # 🔥 Direct command support
                else:
                    processCommand(command)

        except Exception as e:
            print("Sorry, I didn't catch that. Please try again.")