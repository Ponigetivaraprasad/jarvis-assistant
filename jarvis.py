import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import random


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
        speak("Good afternoon! I'm Jarvis, your personal assistant.")
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
        command = r.recognize_google(audio, language='en-in')
        command = command.lower().strip()
        print("User said:", command)
    except Exception as e:
        speak("Sorry, I did not understand that.please repeat.")
        return "None"
    return command
#Handle Commands
def execute_command(command):
    if "youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")
    elif "open calculator" in command:
        speak("Opening calculator...")
        os.system("calc")
    elif "google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "").strip()
        if query:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("Sorry, I could not find any information on that topic.")
        else:
            speak("Please specify a topic to search on Wikipedia.")
    elif "play music" in command:
        music_folder = "C:\\users\\public\\Music"
        songs = os.listdir(music_folder)
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(music_folder, song))
            speak(f"Playing {song}")
        else:
            speak("No music files found in the music directory.")
    elif "who are you" in command:
        speak("I am Jarvis, your personal assistant. I am here to help you with various tasks and make your life easier.")
    elif "who made you" in command:
        speak("I was created by Varaprasad ponigeti sir.")
    elif "open command prompt" in command:
        speak("Opening Command Prompt...")
        os.system("cmd")
    elif "how are you" in command:
        speak("I am just a program, but thank you for asking. How can I assist you today?")


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
                                                        
              
                                                   
