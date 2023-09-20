import code
from distutils.spawn import spawn
from tkinter.ttk import Separator
from unittest import result
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from datetime import date
import wikipedia #pip install wikipedia
import webbrowser
import os
import pywhatkit
import smtplib
import wolframalpha
import config
import sys

from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from youtube import Speak

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! sparsh")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! sparsh")   

    else:
        speak("Good Evening! sparsh")  
    
    speak("hello sparsh")
    speak(".")
    speak("dodo is ready to go, tell me how may I help you")   


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
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

app_id = config.wolframaplpha_id

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xpredator2021@gmail.com', 'sparsh9803')
    server.sendmail('xpredator2021@gmail.com', to, content)
    server.close()

def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()


# this is for some silly question 
        
        if ' who is your father' in query:
            speak("myl father name is sparsh sharma")
            speak("from sharma family")

        elif'date of birth' in query:
            speak("my date of birth is 8 september 2021")
        
        elif'when was you born'in   query:
            speak("my date of birth is 8 september 2021")

        
        elif'what is my sllyabus' in query:
            speak("your sllaybus is ")
            speak("")
        
        elif'how old are you' in query:
            speak("i am 1 years old ")

        elif 'youtube' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from youtube import YouTubeSearch
            YouTubeSearch(query)
        
        elif'google' in query:
            import wikipedia as googleScrap
            query = query.replace("dodo","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("this is what i found on the web ")
            pywhatkit.search(query)

            try:
                result =googleScrap.summary(query,3)
                speak(result)
            
            except :
                speak("No spek data found ")

        elif'RAM 'in query:
            speak("RAM RAM JI ")
        
        elif'hello' in query:
            speak("hello sparsh")
        
        elif'thanks'in query:
            speak("your welcome")
        
        elif'what is papa email id'in query:
            speak("papa email id is ")
            speak("a m m s h 8 0 6 0 @ gmail.com")

        elif'what is my email id'in query:
            speak("your email id is")
            speak("xpredator2021@gmail.com")

        elif'how are you' in query:
            speak("i am fine, sparsh")
            speak("i hope you also fine")

        elif'what are you doing'in query:
            speak("nothing just talking to you ")
        
        elif'nice' in query:
            speak("thanks")

# open thing in web 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open world'in query:
            speak("opening mami youtube channel")
            webbrowser.open("https://www.youtube.com/channel/UCwtwipr91OuUGwGW3Qgoy5Q")
        
        elif 'open studio' in query:
            webbrowser.open("https://studio.youtube.com/channel/UCv4ExSU-9Ye_xGEcEE8dUNw")
            speak("opening studio")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("opening instagram")
        
        elif 'play under' in query:
            webbrowser.open("https://www.youtube.com/watch?v=5dsg-nUJJaM")
            speak("plyaing song")
            speak("enjoy your song")

        elif 'open server' in query:
            webbrowser.open("https://github.com/xpredator202")
            speak("opeing server")

        elif'diljit' in query:
            speak("wait a mint")
            speak(".")
            speak(".")
            speak("ok now i am playing panamera white")
            webbrowser.open("https://www.youtube.com/watch?v=t9JQMV85jyE")

# this is for asking time 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Manav sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening code")
        
        elif 'open word' in query:
            codePath ="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe"
        
        elif 'open excel' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe"
        
        elif'open powerpoint' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe"
        
        elif'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            speak("opeing mail, sparsh")
        
        elif'open papa male'in query:
            webbrowser.open("https://mail.google.com/mail/u/2/#inbox")
            speak("opeing papa mail, sparsh")

        elif'open papa photo' in query:
            codePath="C:\\Users\\Manav sharma\\Videos\\sparsh sharma youtube\\mail work"
        
        elif ' calculate' in query:
            question = query
            answer = computational_intelligence(question)
            speak(answer)
# this is for calculation 

        elif 'calculate the area of rectangle' in query:
            speak("tell me the length of the object")
            query=takeCommand()
            l=int(query)
            speak("tell me the breadth of the object ")
            query2=takeCommand()
            b=int(query2)
            ar=l*b
            speak("your area of rectangle is")
            speak( ar)
            print(ar)
        
        elif 'calculate the area of square' in query:
            speak("tell me the number")
            a=int(takeCommand())
            rt=a*a
            speak("area of the square is")
            speak( rt)
            print(rt)
        
        elif 'calculate the area of triangle'in query:
            speak("tell me the base of the object")
            query=takeCommand()
            o=int(query)
            speak("tell me the height of the object")
            query2=takeCommand()
            p=int(query2)
            tr=o*p/2
            speak("area of the triangle is")
            speak(tr)
            print(tr)

        elif 'calculate the area of circle'in query:
            speak("tell me the radius of the circle")
            i=int(takeCommand())
            qw=22/7*i*i
            speak("area of the circle is ")
            speak(qw)
            print(qw)

        elif 'calculate the area of cube'in query:
            speak("tell me the edge of the cube")
            r=int(takeCommand())
            rq=6*r*r
            speak("area of the cube is")
            speak(rq)
            print(rq)
        
        elif 'calculate the area of cuboid'in query:
            speak("tell me the hight of the object")
            query=takeCommand()
            w=int (query)
            speak("tell me the lenth of th object")
            query2=takeCommand()
            q=int(query2)
            speak("tell me the base of the object")
            query3=takeCommand()
            wq=int(query3)
            qwq=2*w*q+wq 
            speak("area of the cubeoid is ")
            speak(qwq)
            print(qwq) 
        
        elif'sum'in query:
            speak("ok then")
            speak("tell me the first number ")
            query=takeCommand()
            ee=int(query)
            speak("tell me the second number")
            query2=takeCommand()
            eee=int(query2)
            eeee=ee+eee
            speak(eeee)
            print(eeee)
        
        elif'subtraction'in query:
            speak("ok ")
            speak("tell me the first number")
            query=takeCommand()
            rr=int(query)
            speak("tell me the 2 number")
            query2=takeCommand()
            rrr=int(query2)
            rrrr=rr-rrr
            speak(rrrr)
            print(rrrr)
        
        elif'multiply'in query:
            speak("ok")
            speak("tell me the first number")
            query=takeCommand()
            yy=int(query)
            speak("tell me the no that i have multiply this ")
            query2=takeCommand()
            yyy=int(query2)
            yyyy=yy*yyy
            speak("ok your answer is ")
            speak(yyyy)
            print(yyyy)
         
        elif'divide'in query:
            speak("ok ")
            speak("tell me the divisor")
            query=takeCommand()
            n=int(query)
            speak("tell me the divident")
            query2=takeCommand()
            nn=int(query2)
            nnn=n/nn
            speak("your reminder is ")
            speak(nnn)
            print(nnn)
        
        elif' good at 'in query:
            speak("are you a dum i am a computer it's a esay job for me ")
            speak("per thank's tarif ker ne ka liya ")

# to explain some topics about science and other 

        elif 'human eye'in query:
            speak("ok sparsh")
            speak("i have all information that you need")
            speak("let me open a video sparsh")
            speak("in which lang do you prefer  sparsh")
            query=takeCommand()
        if 'hindi 'in query:
                speak("ok sparsh ")
                speak("i am plaing video in hindi")
                webbrowser.open("https://www.youtube.com/watch?v=EqFjhsMlXXQ")
        elif'english'in query:
                speak("ok sparsh")
                speak("i am playing video in englsh ")
                webbrowser("https://www.youtube.com/watch?v=uuWb1L2Vwsk")

        elif 'altimeter' in query:
                speak("It is used to Measures altitudes,")
                speak("and")
                speak("used in aircraft")
            
        elif'ammeter' in query:
                speak("It is used to Measures strength of electric current")
            
        elif'anemometer'in query:
            speak("it is used to measures force and velocity of wind and determines its directions")

        elif'audiometer'in query:
            speak("it is used to measures intensity of sound ")
        
        elif'Barograph'in query:
            speak("it is used to measures continuos recording of atmospherc pressure ")
        
        elif'barometer'in query:
            speak("it is used to measures atmospheric pressure")
        
        elif'binoculars'in query:
            speak("it is used to measures to viw distant objects")
        
        elif'callipers'in query:
            Speak("it is used to measures inner and outer diameters of bodies")
        
        elif'calorimeter'in query:
            speak("it is ued to measure quantites of heat ")

        elif'dilatometer' in query:
            speak("it is used to measure changes in volume of substances")
        
        elif'dyanamo' in query:
            speak("to convrt mechanical energy into electric current ")
        

            
        elif 'human heart' in query:
                speak("ok sparsh")
                
# this is for email 

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ammsh8060@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sparsh . I am not able to send this email") 