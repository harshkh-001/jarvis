import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices" ,voices[0].id)
# print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    



def wishme():
    hour = int(datetime.datetime.now().hour)

    if(hour>=0 and hour<12):
        speak("Good morning sir")
        
    elif(hour>=12 and hour<17):
        speak("Good afternoon sir")
        
    elif(hour>=17 and hour<24):
        speak("Good evening sir")
        
    else :
        speak("good night sir")
        
if __name__== "__main__" :
    wishme()
    speak("How can i help you")
        
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio , language="en-in")
        # amazon = r.recognize_amazon(audio , language = "en-in")
        print(f"user said : {query}\n")
        # print(f"user said (by amazon): {amazon}\n")
    except Exception as e:
        print("say that again please... ")
        # speak("say that again please... ")
        return "none"
        # return take_command()
    
    return query

def sendmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('newtry443@gmail.com' , 'Password123@')
    server.sendmail('newtry443@gmail.com' ,to ,content )
    server.close()
# take_command()

if __name__ == "__main__":
    
    while True:
        query = take_command().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        elif "exit" in query  or  "quit" in query  or  "by jarvis" in query  or  "by" in query  or  "good night" in query or "goodbye" in query:
            speak("goodbye sir have a nice day")
            exit()
            quit()
            
        elif "open youtube" in query:
            webbrowser.open('https://www.youtube.com/')
            
        elif "open google" in query:
            webbrowser.open('https://www.google.com/')
            
        elif "open mail" in query:
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
            
        elif "open classroom" in query:
            webbrowser.open('https://classroom.google.com/')
            
        elif "play song" in query or "play songs" in query or "play music" in query or "play musics" in query :
            
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            i = random.randint(0,3)
            os.startfile(os.path.join(music_dir , songs[i]))
            
        elif "tell time" in query or "time please" in query or "what is time" in query :
            speak("sure sir, the current time is")
            print(datetime.datetime.now().strftime("%H:%M:%S"))
            speak(datetime.datetime.now().strftime("%H:%M:%S"))
            
        elif "tell date" in query or "date please" in query or "todays date" in query or "today date" in query :
            speak("sure sir, todays date is")
            print(datetime.datetime.now().strftime("%d/%m/%y"))
            speak(datetime.datetime.now().strftime("%m/%d/%y"))
             
        elif "open code" in query :
            CodePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(CodePath)
            
        elif "open chrome" in query :
            CodePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(CodePath)
            
        # elif "mail to harsh" in query :
        #     try:
        #         speak("What should i say to harsh in mail")
        #         content = take_command()
        #         To = "harshkhandelwal1245@gmail.com"
        #         sendmail(To , content)
        #         speak("email has been send to harsh")
            
        #     except Exception as e:
        #         print(e)
        #         speak("sorry unable to send mail")
        
        
            
        speak("do you want me to do anything else for you sir")