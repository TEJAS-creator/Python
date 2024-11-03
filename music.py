import pywhatkit
import speech_recognition as sr

# Function to listen to voice command
def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return None

if __name__ == "__main__":
    command = listen_to_command()
    if command:
        pywhatkit.playonyt(command)
