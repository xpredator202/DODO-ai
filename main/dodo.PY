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
from selenium import webdriver
from selenium.webdriver.common.by import By
import config
from time import sleep
import psutil
import requests
import wolframalpha
import pyautogui
import pyaudio
from PIL import Image
import config
import cv2
import mediapipe as mp 
import warnings

warnings.filterwarnings("ignore")
warnings.warn("second example of warning!")
hour = int(datetime.datetime.now().hour)
strTime= datetime.datetime.now().strftime("%H:%M:%S")
battery= psutil.sensors_battery()
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voicespeed = 200
engine.setProperty('rate',voicespeed)


GREETINGS = ["hello dodo","dodo","wake up dodo","you there dodo","time to work dodo","hey dodo","ok dodo","are you there"]
GREETINGS_RES= ["always there for you ","i am ready", "your wish is my command, let's go","how can i help you","i am online and ready to go"]
EMAIL_DIC ={
    'myself':'xpredator2021@gmail.com',
    'my offical email' : 'xpredator2021@gmail.com',
    'my second email' : 'ammsh8060@gmail.com',
}
pkq={
    'sometimes its not ego, its self respect,',
    'im loyal because its in me not because i need you',
    'self respect isnt important thing its everything',
    'its so nice to listen to lies when you know the truth',
    'betrayal  never comes from enemis',
    'dream as if you live forever, lives as you die today', 
    'its so nice to listen to lies when you know the truth',
    'silence is the best answer who dont value your word',
    'he looked at me in the wrong way, its not a good idea to look at tommy shebly the wrong way',
    'confidence is build by what you fear. ',
    'be like glass if they break you cut them',
    'a fish with its mouth closed never gets caught',
    'let people talk behind your back they are behind u for a reason',
    'revenge has no expire date i will be back when i am ready.',
    'forgive your enimes but never forgive there name',
    "turn anxiety into excitement like a spartan against million persians.",
    "there is a quote by itachi uchhia 'if a men cries he is not weak he just has been strong for too long",
    "there is a quote by luffy that forgetting  is like a wound the wound may heal but it has already leave a scare",
    "there is a quote by joker he said in there last moment people show you who they really are",
    "there is a quote by thanos the hardest choice requires a strong will",
    "there is a quote by kankei there are heartless peopel who cared too much",
    "there is a quote by conor mcgregor look with all due respect to everyone fuck everyone i'm just here for my own, for my own self",
    "the number you have dialed doesn't give a fuck",
    "there is a quote by ghost be careful who you trust sergeant people you know can hurt you the most",
    "don't ever think i need you in my life. we once didn't know eachother and i was doing just fine",
    "move in silence speak when it's time to say chackmate",
    "when the line gets straght eveyone will love you all of sudden",
    "when you realise that no one remember you after your death at that point you forget about what other people think",
    
}




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........... ")
        r.pause_threshold =1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-us',)
        print(f"User Said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please ..... ")
        return "None"
    return query


def wishMe():
    speak("welcome back sir")

    if hour>=0 and hour<12:
        speak(f"Good Morning! sparsh")
        print(f"Good Morning! sparsh")

    elif hour>=12 and hour<18:
        speak(f"Good AfterNoon! sparsh")
        print(f"Good AfterNoon! sparsh")
    else:
       print(f"Good Evening! sparsh ")
       speak(f"Good Evening! sparsh")
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        if 'time' in query:
            speak(f"sparshthe time is {strTime}")
        
        elif'build'in query:
            speak("my creater is sparsh sharma")
        
        elif'good morning'in query:
          if hour>=0 and hour<12:
            speak("thank you sir")
            print("thank you sir")
            speak("have a nice day sir")
            print("have a nice day sir")
          else:
            speak("it's not morning sir")
            print("it's not morning sir")
            speak(f"sir the time is {strTime}")
            print(f"sir the time is {strTime}")
            speak("according to the time")
            print("according to the time")
            if hour>=12 and hour<18:
             speak(f"it's  AfterNoon! sparsh")
             print(f"it's  AfterNoon! sparsh")
            else:
             print(f"it's  Eveining! sparsh ")
             speak("it's eveining sir ")
        
        elif'hello to baba' in query or 'hello  to' in query:
            speak("hello baba ji")
            speak("how are you baba ji")
            speak("how's your health")

        elif'battery'in query or 'how much battery'in query or 'battery life'in query or 'power'in query:
            speak("ok sir let me check ")
            speak("accound to the statics")
            print("Battery percentage : ", battery.percent)
            speak(f"the battery percentage is {battery.percent}")
            print("Power plugged in : ", battery.power_plugged)
            speak(f"the power plugged in{battery.power_plugged}")
            print("Battery left : ", convertTime(battery.secsleft))
            speak(f"battery left: {convertTime(battery.secsleft)}")

        elif'good after Noon 'in query or 'good afternoon' in query or 'good afterNoon' in query:
           if hour>=12 and hour<18:
            speak("thank you sir")
            print("thank you sir")
            speak("best of luck for your work sir")
            print("best of luck for your work")
           else:
            speak("sir it's not afterNoon")
            print("sir it's not afterNoon")
            speak(f"sir the time is {strTime}")
            print(f"sir the time is {strTime}")
            speak("according to the time")
            print("according to the time")
            if hour>=0 and hour<12:
                speak("it's morning sir")
                print("it's morning sir")
            else:
                print("it's evening sir")
                speak("it's evening sir")

        elif'remind me'in query or 'set a reminder'in query:
            speak("what shall i remind you sir")
            import time
            print("What shall I remind you about?")
            text = takecommand()
            print("In how many minutes? sir")
            speak("In how many minutes? sir")
            tin=takecommand()
            local_time = tin
            local_time1 = local_time * 60
            time.sleep(local_time1)
            print(text)
            speak(text)

        elif'good evening'in query :
            speak("thank you sir")
            print("thank you sir")
            speak("what's your plan for evening sir")
            time.sleep(3)
            crlf = takecommand()
            if "nothing"in crlf or "no plans" in query:
                speak("i think you are taking rest")
                speak("that's good sir")
                speak("can i play some melodi songs for you sir")
                ln=takecommand()
                if"yes"in ln:
                    speak("that's nice")
                    speak("i make a playlist for you hope you like it")
                    webbrowser.open("https://www.youtube.com/watch?v=V-huZdv9ODQ&list=RDV-huZdv9ODQ")
                    speak("enjoy your evening sir")
                    speak("if you need any thing just call me")
                else:
                    speak("no problem sir")
                    speak("if you need any thing just call me")
            else:
                speak("that's a good plan, sir")
                speak("if you need help just tell me i will help you")
            
        elif'play song'in query or "play some song"in query or "just rock " in query:
            speak("ok sir")
            speak("just tell me which type of music do you need")
            utf=takecommand()
            if 'sad'in utf or 'mood off' in utf:
                speak("ok sir")
                speak("i have a best playlist for you ")
                webbrowser.open("https://www.youtube.com/watch?v=9xG5aPvrS-k&list=RD9xG5aPvrS-k&start_radio=1")
            elif 'dancing mood'in utf or 'good mood' in utf:
                speak("ok sir")
                speak("i have a best playlist for you")
                webbrowser.open("https://www.youtube.com/watch?v=V-huZdv9ODQ&list=RDV-huZdv9ODQ")
            elif'motivational ' in utf or 'code'in utf:
                speak("ok sir")
                speak("i have a best playlist for you")
                webbrowser.open("https://www.youtube.com/watch?v=Zn-VQ-B1ODA&list=RDZn-VQ-B1ODA")
            elif'relex' in utf or 'random' in utf:
                speak("ok sir ")
                speak("i have a best playlist for you")
                webbrowser.open("https://www.youtube.com/watch?v=k8i6PC5HohA")

            
        elif'send message'in query:
            speak("ok sir")
            speak("tell me whom do you want to send the message")
            dkk=takecommand()
            
        elif query in GREETINGS:
          speak(random.choice(GREETINGS_RES))

        elif'brother youtube'in query:
            speak(f"ok sparsh")
            speak("opening brother youtube chennel")
            webbrowser.open("https://www.youtube.com/@manav_sharma_")
        
        elif'my youtube'in query:
            speak(f"ok sparsh")
            speak("opening your youtube chennel")
            webbrowser.open("https://www.youtube.com/channel/UCv4ExSU-9Ye_xGEcEE8dUNw")
        
        
        elif'hello' in query:
            speak(random.choice(GREETINGS_RES))
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak(f"opening youtube sparsh")

        elif 'open brave' in query:
            codePath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)
            speak("opening brave")

        elif'close the app' in query or 'close this app'in query or 'close this current app'in query or 'close the current app'in query:
            pyautogui.hotkey('alt','f4')
            speak("closing the currunt app sir")

        elif'shutdown'in query:
            speak("ok sir the system is shutdown in")
            os.system("shutdown -s -t 5") 
            speak("5")
            speak("4")
            speak("3")
            speak("2")
            speak("1")
            speak("0")
            
        
        elif'restart'in query:
            speak("ok sir the system is restart in")
            os.system("shutdown -r -t 5") 
            speak("5")
            speak("4")
            speak("3")
            speak("2")
            speak("1")
            speak("0")
        
        elif'mom want to talk'in query or 'mom has a question' in query or 'mom talk'in query or'mom'in query:
            speak("yes mom")
            speak("do you need any type of help")
            
        
        elif'thank you' in query:
            speak(f"no problem sparsh")
            speak(f"it's my duty")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open world'in query:
            speak(f"opening mami youtube channel sparsh")
            webbrowser.open("https://www.youtube.com/channel/UCwtwipr91OuUGwGW3Qgoy5Q")
        
        elif 'open studio' in query:
            webbrowser.open("https://studio.youtube.com/channel/UCv4ExSU-9Ye_xGEcEE8dUNw")
            speak("opening studio")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak(f"opening instagramsparsh")
        
        elif 'play under' in query:
            webbrowser.open("https://www.youtube.com/watch?v=5dsg-nUJJaM")
            speak("plyaing song")
            speak(f"enjoy your song sparsh")

        elif 'open server' in query:
            webbrowser.open("https://github.com/xpredator202")
            speak(f"opeing serversparsh")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Manav sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak(f"opening code sparsh")
        
        elif'shelby style'in query or 'style'in query:
            speak("perfect")
            codePath = "C:\\Users\\Manav sharma\\sparsh\\.vscode\\main\\thomas shelby.mp4"
            os.startfile(codePath)
            
        elif'diljit' in query:
            speak("wait a mint")
            speak(".")
            speak(".")
            speak(f"ok now i am playing panamera white sparsh")
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
           speak(f"this is what i found on the web sparsh")
           pywhatkit.search(query)
           try :
               result = googleScrap.summary(query,1)
               speak(result)


           except:
             speak(f"no data found sparsh")

        elif ' I am feeling happy 'in query:
            speak("i am happy to hear that ")
        
        elif'leave the topic'in query:
            speak("as you wish sir")
        
        elif'what are you doing'in query:
            speak("nothing much just searching some good for you")
        
        elif'I am  feeling sad'in query:
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
           speak(f"your name is sparsh ")

        elif'wake up'in query:
            speak("i am up sir")
            speak("tell me what can i help you, sir")
        
        elif'my self'in query or 'who is sparsh'in query:
            speak("your name is sparsh sharma")
            speak("his father name is MR. Arun kumar sharma ")
            speak("he is genius")
            speak("he make website like black devil .com")
            speak("there is a lot of inovetion he do like creating me ")
            speak("he is my master, friend and a good partner")

        elif 'are you there 'in query:
            speak("at your service sir")
            speak("what can i do for you sir")
        

            
        elif'no problem'in query:
            speak("ok sir")
            speak("as you wish")


        elif'introduce yourself'in query:
           speak(f"ok sparsh")
           speak("my name is dodo ,I am a A.I which is able to perform task like chat bot, etc. It provides basic functionality for any assistant application. It is based on artificial intelligence, It is also powerful like JARVIS")
        
        elif'who is jarvis'in query:
           speak("J.A.R.V.I.S. (Just A Rather Very Intelligent System) is a fictional character voiced by Paul Bettany in the Marvel Cinematic Universe (MCU) film franchise, based on the Marvel Comics characters Edwin Jarvis and H.O.M.E.R., respectively the household butler of the Stark family and another AI designed by Stark. J.A.R.V.I.S. is an artificial intelligence created by Tony Stark, who later controls his Iron Man and Hulkbuster armor for him. In Avengers: Age of Ultron, after being partially destroyed by Ultron, J.A.R.V.I.S. is given physical form as Vision, physically portrayed by Bettany. Different versions of the character also appear in comics published by Marvel Comics, depicted as AI designed by Iron Man and Nadia van Dyne")

        elif'who is your father'in query:
           speak("my father name is sparsh sharma ")
        
        elif'ram'in query:
           speak(f"ram ram ji sparsh")
           speak("ram ram ji to everyone")

        elif'radhe'in query:
            speak(f"radhey radhey sparsh")
            speak("radhey radhey everyone")
        
        elif'how are you 'in query:
            speak("i am fine")
            speak(f"thank you for asking me sparsh")
        
        elif"close the note" in query or "close notepade" in query:
         speak(f"okey sparsh,closing notepad")
         os.system("taskill /f /im notepad++.exe")

        elif "joke" in query:
         joke = pyjokes.get_joke()
         print(joke)
         speak(joke)
       
        elif 'switch the window'in query or 'switch window' in query or 'change window' in query or 'change screen' in query:
            speak(f"okay sparsh, switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
       
        elif 'take screenshot' in query or "take a screenshot" in query or 'capture the screen'in query or 'take a ss'in query or 'take ss' in query:
            speak("by what name do you want me to save the screenshot?")
            name = takecommand()
            speak(f"alrightsparsh, taking the screen shot")
            img = pyautogui.screenshot()
            name2 = f"{name}.png"
            img.save(name2)
            speak("The screenshot has been succesfully captured")

        elif'camera' in query or "video storage" in query or 'gallery'in query:
            speak("ok sir")
            speak("opening gallery ")
            codepath = 'C://Users//Manav sharma//Pictures//Camera Roll'
            os.open(codepath)

        elif "show me the screenshot" in query:
            try:
                img = Image.open("C://Users//Manav sharma//Pictures//Screenshots//"+name)
                img.show(img)
                speak(f"Here it is sparsh")
                time.sleep(2)

            except IOError:
                speak(f"sorrysparsh, i am unable to display the screenshot")

        elif "hide all files" in query or "hide this folder" in query:
            os.system("attrib +h /s /d")
            speak(f"sparsh, all the files in this folder are now hidden")
        
        elif "visible" in query or "make files visisble" in query:
            os.system("attrib -h /s /d")
            speak(f" sparsh, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")
        
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
            speak(f"ok sparshwhat is the number")
            query1=takecommand()
            w=int(query1)
            ww=w*w
            speak(f"the area of this square is{ww}, sparsh")
            print(f"the area of this square object is {ww},sparsh")
        
        elif'area of trapezium' in query:
            speak(f"ok sparsh tell me the first base of this trapezoid object")
            query1= takecommand()
            e=int(query1)
            speak(f"ok i got the first base ,now sparsh tell me the 2 base of this trapezoid object")
            query2=takecommand()
            ee=int(query2)
            speak(f"now tell me the Height of this trapezoid object")
            query3=takecommand()
            eee=int(query3)
            eeee=e+ee/2*eee
            speak(f"the area of this trapezium object is {eeee},sparsh")
            print(f"the area of this trapezium object is {eeee}, sparsh")

        elif 'area of triangle' in query:
            speak(f"ok sparsh tell me the base of the triangular object")
            query1 =takecommand()
            r=int(query1)
            speak(f"ok i got the base sparsh, now tell me the height of the object")
            query2 =takecommand()
            rr=int(query2)
            rrr=r*rr/2
            speak(f"the area of this object is {rrr}, sparsh")
            print(f"the area of this object is {rrr}, sparsh")

        elif'area of circle'in query:
            speak(f"ok sparsh tell me the radius of the circle")
            query1=takecommand()
            t=int(query1)
            tt=22/7*t*t
            speak(f"the area of this object is {tt},sparsh")
            print(f"the area of this object is {tt},sparsh")

        elif'area of the cylinder'in query:
            speak(f"ok sparsh , then tell me the radius of the object")
            query1=takecommand()
            y=int(query1)
            speak("ok now tell me the height of the object ")
            query2=takecommand()
            yy=int(query2)
            yyy=2*22/7*y*yy+2*22/7*y*y
            speak(f"the area of this object is {yyy},sparsh")
            print(f"the area of this object is {yyy}, sparsh")
        
        elif'area of  cube'in query:
            speak(f"oksparsh, then tell me the edge of the object")
            query1=takecommand()
            u=int(query1)
            uu=6*u*u
            speak(f"the area of this object is{uu},sparsh")
            print(f"the area of this object is{uu},sparsh")

        

        elif "goodbye" in query or "offline"in query or "bye"in query or "i have to go " in query:
            speak(f"alright sparsh, going offline . it was nice working with you")
            sys.exit()
        
        elif'help'in query:
            speak("tell me which type of help do you need")
            tree = takecommand()
            if 'work'in tree:
                speak(f"don't ware sparsh")
                speak("just tell me the topic")
                speak("now tell me do you want to watch video or you want to search me on google or in wikipedia")
                xx= takecommand()
                if "video" in xx:
                    Query = query.replace("dodo", "")
                    QUERY = Query.replace("youtube search","")
                    from youtube import YouTubeSearch
                    YouTubeSearch(query)
                elif "google" in xx:
                   query = query.replace("dodo","")
                   query = query.replace("google search","")
                   query = query.replace("google","")
                   speak(f"this is what i found on the websparsh")
                   pywhatkit.search(query)