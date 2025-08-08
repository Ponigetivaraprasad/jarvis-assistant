import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()
# Speech recognisition setup
def speak(text):
    engine.say(text)
    engine.runAndWait()
# wishing user based on time
def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening! I'm jarvis, your personal assistant.")
    speak("I am Jarvis, your personal assistant. How can I help you today?")
#Take command from the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"you said:{command}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.please repeat.")
        return "None"
    return command.lower()
#Handle Commands
def execute_command(command):
    if "youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "open notepad" in command:
        speak("Opening Notepad...")
        os.system("notepad")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I am sorry, I cannot perform that action. Please try again.")
# Main function to run the assistant
if __name__ == "__main__":
    wish_user()
    while True:
        command = take_command()
        if command != "None":
            execute_command(command)
                                                        
              
                                                   
