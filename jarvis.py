import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser 
import os
import smtplib
import pyrebase
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['date.converter'] = 'concise'
firebaseConfig ={"apiKey": "AIzaSyBkOV6QB9l39zU0qerJes5pgPGimiaxJXw",

  "authDomain": "project-97898.firebaseapp.com",

   "projectId": "project-97898",

   "storageBucket": "project-97898.appspot.com",

   "messagingSenderId": "733908495399",

   "appId": "1:733908495399:web:480b8a189bdff4194bb202",

    "measurementId": "G-P9CJXT2MK5"}
                




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hey Yashwanth, I am Jarvis. Please tell me how may I help you Sir.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        
        if "Hey Jarvis" in query:
            speak("Yes Sir")     
        
        elif "You up" in query:
            speak("always up for you sir")

        elif "hey man you up" in query:
            speak("Yeah sir")

        elif "you thinking what I am thinking" in query:
            speak("Yes Sir, Let's make it possible")

        elif "are you joking" in query:
            speak("No sir I am serious")
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Here is your website Sir")
        
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Here is your website Sir")

        
        elif 'open my channel' in query:
            webbrowser.open("https://www.youtube.com/channel/UC6f0wsVNVzOG0AVavqCho5g")   
            speak("Here is your Channel Sir")
        
        
        elif 'play pagal' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            speak("Here is your song Sir..Enjoy")
            os.startfile(os.path.join(music_dir, songs[1]))
            
        elif 'play dj tillu' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Here is your song Sir..Enjoy")    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'pushpa' in query:
            music_dir = 'D:\Music'
            print(songs)
            speak("Here is your song Sir..Enjoy")    
            os.startfile(os.path.join(music_dir, songs[2]))    

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Yashwanth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to palli' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "YashyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Yash . I am not able to send this email")    

        elif 'open my folder' in query:
            folderpath = "D:\Softwares"
            os.startfile(folderpath)            
        
        elif 'Open spot' in query: 
            webbrowser.open("spotify.com")

        elif "Srishanth" in query:
            speak("Srishanth")
        elif "control bluetooth" in query:
            speak("Shut the Hell How can I access your Files without Bluetooth")
        
 
        elif "my age" in query:
            birthday = datetime.date(2005, 2, 5)
            today = datetime.date.today()
            age_in_days = (today - birthday).days
            print(age_in_days)
            speak("Sir Your age is" , age_in_days)  
        

        elif "Wish Nani" in query:
            print("Hello Nani, How are you??")
            speak("Hello Nani, How are you?")

        elif "show my logo" in query:
            logo_dir = 'D:\pics'
            logo = os.listdir(logo_dir)
            speak('Opening Logo')
            os.startfile(os.path.join(logo_dir, logo[4]))

        elif "whats is my device name" in query:
            speak('Sir Your Device using is a Laptop, Its name is DELL G15 5515')

        elif "what are my specifications" in query:
            speak('Sir ther the laptop specifications are Ryzen 5 5600H Processor with Zen 3, architecture, RTX 3050 with 4GB of VRAM ')

        elif "get my details" in query:
            speak("Sir Got your details via aadhar card")

        elif "wish my aunt" in query:
            speak("Hello Hymavathi garu")

        elif "wish my uncle" in query:
            speak("Hello Nagarjuna Rao garu")

        elif "open my movies folder" in query:
            moviepath = "D:\Movies"
            os.startfile(moviepath)
        
        elif "complete my code" in query:
            speak("Sir your code has been completed for Jarvis AI")
        
        elif "tell me a joke" in query:
            speak("Knock Knock")
            if "who's there" in takeCommand():
                speak("tank")
            if "tank who?" in takeCommand():
                    speak("Your welcome") 

        elif "go to sleep" in query:
           codePath = "C:\\Users\\Yashwanth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.close(codePath)

        elif "When will the firebase cloud will reopen after breakdown" in query:
            speak("Sir the Server Breakdown will be fixed by 12pm")
            print("Sir the Server Breakdown will be fixed by 12pm")

        