from youtube import Speak
import tkinter
import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import time 
import sys 
import pyjokes
import pywhatkit
import urllib.parse
import pprint
import random
import requests
import wolframalpha
import pyautogui
import pyaudio
from PIL import Image
import config
import warnings

warnings.filterwarnings("ignore")
warnings.warn("second example of warning!")



engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


GREETINGS = ["hello dodo","dodo","wake up dodo","you there dodo","time to work dodo","hey dodo","ok dodo","are you there"]
GREETINGS_RES= ["always there for you ","i am ready", "your wish is my command, let's go","how can i help you","i am online and ready to go"]
EMAIL_DIC ={
    'myself':'xpredator2021@gmail.com',
    'my offical email' : 'xpredator2021@gmail.com',
    'my second email' : 'ammsh8060@gmail.com',
}


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........... ")
        r.pause_threshold =1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in',)
        print(f"User Said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please ..... ")
        return "None"
    return query


speak("hello there,")
speak("please tell me what should i call you")
userName= takecommand()
speak("ok, i will call you"+userName)
speak("by the way that's a nice name")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning! {userName}")
        print(f"Good Morning! {userName}")

    elif hour>=12 and hour<18:
        speak(f"Good AfterNoon! {userName}")
        print(f"Good AfterNoon! {userName}")
    else:
        speak(f"Good Evening! {userName}")
        print(f"Good Eveining! {userName} ")

def login_face_system():
    import cgi 
    from base64 import b64decode
    import face_recognition
    formData=cgi.FieldStorage()
    face_match=0
    



if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
    
        if 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{userName}the time is {strTime}")
        
        elif'build'in query:
            speak("my creater is sparsh sharma")

        elif query in GREETINGS:
          speak(random.choice(GREETINGS_RES))

        elif'brother youtube'in query:
            speak(f"ok {userName}")
            speak("opening brother youtube chennel")
            webbrowser.open("https://www.youtube.com/@manav_sharma_")
        
        elif'my youtube'in query:
            speak(f"ok{userName}")
            speak("opening your youtube chennel")
            webbrowser.open("https://www.youtube.com/channel/UCv4ExSU-9Ye_xGEcEE8dUNw")
        

        
        elif'hello' in query:
            speak(random.choice(GREETINGS_RES))
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak(f"opening youtube{userName}")

        elif 'open brave' in query:
            codePath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)
            speak("opening brave")
        
        elif'thank you' in query:
            speak(f"no problem {userName}")
            speak(f"it's my duty")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open world'in query:
            speak(f"opening mami youtube channel{userName}")
            webbrowser.open("https://www.youtube.com/channel/UCwtwipr91OuUGwGW3Qgoy5Q")
        
        elif 'open studio' in query:
            webbrowser.open("https://studio.youtube.com/channel/UCv4ExSU-9Ye_xGEcEE8dUNw")
            speak("opening studio")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak(f"opening instagram{userName}")
        
        elif 'play under' in query:
            webbrowser.open("https://www.youtube.com/watch?v=5dsg-nUJJaM")
            speak("plyaing song")
            speak(f"enjoy your song{userName}")

        elif 'open server' in query:
            webbrowser.open("https://github.com/xpredator202")
            speak(f"opeing server{userName}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Manav sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak(f"opening code{userName}")

        elif'diljit' in query:
            speak("wait a mint")
            speak(".")
            speak(".")
            speak(f"ok now i am playing panamera white{userName}")
            webbrowser.open("https://www.youtube.com/watch?v=t9JQMV85jyE")
        
        elif'work'in query:
            speak("ok wait, let  me prepaer your system  ")
            speak("let's go sir")
            webbrowser.open("https://github.com/xpredator202")
            webbrowser.open("https://www.youtube.com/watch?v=Zn-VQ-B1ODA&list=RDZn-VQ-B1ODA")
            codePath = "C:\\Users\\Manav sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)



        elif'youtube' in query:
           Query = query.replace("dodo", "")
           QUERY = Query.replace("youtube search","")
           from youtube import YouTubeSearch
           YouTubeSearch(query)
        
        elif'google' in query:
           import wikipedia as googleScrap
           query = query.replace("dodo","")
           query = query.replace("google search","")
           query = query.replace("google","")
           speak(f"this is what i found on the web{userName}")
           pywhatkit.search(query)
           try :
               result = googleScrap.summary(query,1)
               speak(result)


           except:
             speak(f"no data found {userName}")

        elif 'happy 'in query:
            speak("i am happy to hear that ")
            speak("do you want to l")
        
        elif'leave the topic'in query:
            speak("as you wish sir")
        
        elif'what are you doing'in query:
            speak("nothing much just searching some good for you")
        
        elif'sad'in query:
            speak("can i play some song for you ")
            speak("it will help you to feel good ")
            cc=takecommand()
            if 'yes' in cc:
                speak("that a nice choice")
                speak("now i am playing some songs for you")
                webbrowser.open="https://www.youtube.com/watch?v=Zn-VQ-B1ODA&list=RDZn-VQ-B1ODA"
            elif'no'in cc:
                speak("ok as you wish")
                speak("sir")
            
        

        elif'what is your name' in query:
           speak("my name is dodo")
           speak("and i know your name")
           speak(f"your name is {userName} ")

        elif'introduce yourself'in query:
           speak(f"ok{userName}")
           speak("my name is dodo ,I am a A.I which is able to perform task like chat bot, etc. It provides basic functionality for any assistant application. It is based on artificial intelligence, It is also powerful like JARVIS")
        
        elif'who is jarvis'in query:
           speak("J.A.R.V.I.S. (Just A Rather Very Intelligent System) is a fictional character voiced by Paul Bettany in the Marvel Cinematic Universe (MCU) film franchise, based on the Marvel Comics characters Edwin Jarvis and H.O.M.E.R., respectively the household butler of the Stark family and another AI designed by Stark. J.A.R.V.I.S. is an artificial intelligence created by Tony Stark, who later controls his Iron Man and Hulkbuster armor for him. In Avengers: Age of Ultron, after being partially destroyed by Ultron, J.A.R.V.I.S. is given physical form as Vision, physically portrayed by Bettany. Different versions of the character also appear in comics published by Marvel Comics, depicted as AI designed by Iron Man and Nadia van Dyne")

        elif'who is your father'in query:
           speak("my father name is sparsh sharma ")
        
        elif'ram'in query:
           speak(f"ram ram ji{userName}")
           speak("ram ram ji to everyone")

        elif'radhe'in query:
            speak(f"radhey radhey {userName}")
            speak("radhey radhey everyone")
        
        elif'how are you 'in query:
            speak("i am fine")
            speak(f"thank you for asking me {userName}")
        
        elif"close the note" in query or "close notepade" in query:
         speak(f"okey{userName},closing notepad")
         os.system("taskill /f /im notepad++.exe")

        elif "joke" in query:
         joke = pyjokes.get_joke()
         print(joke)
         speak(joke)
       
        elif 'swtch the window'in query or 'switch window' in query or 'change window' in query or 'change screen' in query:
            speak(f"okay{userName}, switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
       
        elif 'take screenshot' in query or "take a screenshot" in query or 'capture the screen'in query or 'take a ss'in query or 'take ss' in query:
            speak("by what name do you want me to save the screenshot?")
            name = takecommand()
            speak(f"alright{userName}, taking the screen shot")
            img = pyautogui.screenshot()
            name = f"{name}.png"
            img.save(name)
            speak("The screenshot has been succesfully captured")

        elif "show me the screenshot" in query:
            try:
                img = Image.open("C://Users//Manav sharma//Pictures//Screenshots//"+name)
                img.show(img)
                speak(f"Here it is{userName}")
                time.sleep(2)

            except IOError:
                speak(f"sorry{userName}, i am unable to display the screenshot")

        elif "hide all files" in query or "hide this folder" in query:
            os.system("attrib +h /s /d")
            speak(f"{userName}, all the files in this folder are now hidden")
        
        elif "visible" in query or "make files visisble" in query:
            os.system("attrib -h /s /d")
            speak(f"{userName}, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")
        
        elif'area of rectangle' in query:
            speak("let me prepare my self")
            speak("now first")
            speak("tell me the length of the object")
            query1 = takecommand()
            q=int(query1)
            speak("now, tell me the breath of the object")
            query2=takecommand()
            qq=int(query2)
            qqq=q*qq
            speak(qqq)
            print(qqq)

        elif'area of square' in query:
            speak(f"ok {userName}what is the number")
            query1=takecommand()
            w=int(query1)
            ww=w*w
            speak(f"the area of this square is{ww}, {userName}")
            print(f"the area of this square object is {ww},{userName}")
        
        elif'area of trapezium' in query:
            speak(f"ok {userName} tell me the first base of this trapezoid object")
            query1= takecommand()
            e=int(query1)
            speak(f"ok i got the first base ,now{userName}tell me the 2 base of this trapezoid object")
            query2=takecommand()
            ee=int(query2)
            speak(f"now tell me the Height of this trapezoid object")
            query3=takecommand()
            eee=int(query3)
            eeee=e+ee/2*eee
            speak(f"the area of this trapezium object is {eeee},{userName}")
            print(f"the area of this trapezium object is {eeee}, {userName}")

        elif 'area of triangle' in query:
            speak(f"ok {userName} tell me the base of the triangular object")
            query1 =takecommand()
            r=int(query1)
            speak(f"ok i got the base{userName}, now tell me the height of the object")
            query2 =takecommand()
            rr=int(query2)
            rrr=r*rr/2
            speak(f"the area of this object is {rrr}, {userName}")
            print(f"the area of this object is {rrr}, {userName}")

        elif'area of circle'in query:
            speak(f"ok {userName}tell me the radius of the circle")
            query1=takecommand()
            t=int(query1)
            tt=22/7*t*t
            speak(f"the area of this object is {tt},{userName}")
            print(f"the area of this object is {tt},{userName}")

        elif'area of the cylinder'in query:
            speak(f"ok {userName} , then tell me the radius of the object")
            query1=takecommand()
            y=int(query1)
            speak("ok now tell me the height of the object ")
            query2=takecommand()
            yy=int(query2)
            yyy=2*22/7*y*yy+2*22/7*y*y
            speak(f"the area of this object is {yyy},{userName}")
            print(f"the area of this object is {yyy}, {userName}")
        
        elif'area of  cube'in query:
            speak(f"ok{userName}, then tell me the edge of the object")
            query1=takecommand()
            u=int(query1)
            uu=6*u*u
            speak(f"the area of this object is{uu},{userName}")
            print(f"the area of this object is{uu},{userName}")

        

        elif "goodbye" in query or "offline"in query or "bye"in query or "i have to go " in query:
            speak(f"alright {userName}, going offline . it was nice working with you")
            sys.exit()
        
        elif'help'in query:
            speak("tell me which type of help do you need")
            tree = takecommand()
            if 'work'in tree:
                speak(f"don't ware{userName}")
                speak("just tell me the topic")
                xx= takecommand()
                speak("now tell me do you want to watch video or you want to search me on google or in wikipedia")
                if "video" in xx:
                    Query = query.replace("dodo", "")
                    QUERY = Query.replace("youtube search","")
                    from youtube import YouTubeSearch
                    YouTubeSearch(query)
                elif "google" in xx:
                   query = query.replace("dodo","")
                   query = query.replace("google search","")
                   query = query.replace("google","")
                   speak(f"this is what i found on the web{userName}")
                   pywhatkit.search(query)

