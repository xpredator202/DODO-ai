from youtube import Speak
import tkinter
import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import time 
import smtplib
import insta 
import sys 
from selenium import webdriver
from selenium.webdriver.common.by import By
import config
from time import sleep
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
import cv2
import mediapipe as mp 
import warnings
import cgi 
from base64 import b64decode
import psutil
import numpy as np 

hour = int(datetime.datetime.now().hour)
strTime= datetime.datetime.now().strftime("%H:%M:%S")
option= webdriver.ChromeOptions()
option.headless = True
driver = webdriver.Chrome()
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voicespeed = 200
battery = psutil.sensors_battery()
engine.setProperty('rate',voicespeed)


GREETINGS = [
    "hello ather ","ather ","wake up ather ","you there ather ","time to work ather ","hey ather ","ok ather ","are you there"]
GREETINGS_RES= [
    "always there for you sir ","i am ready", "your wish is my command, let's go","hello sir, how can i help you","i am online and ready to go, sir"]
EMAIL_DIC ={
    'myself':'xpredator2021@gmail.com',
    'my offical email' : 'xpredator2021@gmail.com',
    'my second email' : 'ammsh8060@gmail.com',
}

#quet 
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

# this is for speak 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# takeing comand 
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xpredator2021@gmail.com', 'Sparsh9803')
    server.sendmail('xpredator2021@gmail.com', to, content)
    server.close()

# wishme 
def wishMe():
    speak("welcome back sparsh")
    if hour>=0 and hour<12:
        speak(f"Good Morning! sparsh")
        print(f"Good Morning! sparsh")

    elif hour>=12 and hour<18:
        speak(f"Good AfterNoon! sparsh")
        print(f"Good AfterNoon! sparsh")
    else:
       print(f"Good Evening! sparsh ")
       speak("Good evening sparsh")

# instagram

   
# time cnvert for battery 
def convertTime(seconds):
     minutes, seconds = divmod(seconds,60)
     hours, minutes =divmod(minutes,60)
     return "%d:%02d:%02d" % (hours, minutes, seconds)


# main work
wishMe()
while True:
        query = takecommand().lower()

    
        if 'time' in query:
            speak(f"sparsh the time is {strTime}")

        elif  'repeat' in query:
            speak("what do you want me to repeat sir ")
            ind=takecommand()
            query = query.replace("","")
            query = query.replace("you","")

            speak(ind)
        
        elif 'email to papa' in query or 'email to daddy'in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "ammsh8060@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email") 

        elif 'email to manav' in query or 'email to manav bhi'in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "smanav3003@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")     
        
        elif'build'in query:
            speak("my creater is sparsh sharma")

        elif'they call me lucky'in query or 'lucky'in query:
            speak("don't call him lucky if he is working while you are sleeping ")
# save a number in google contaect
        elif'save a number 'in query or 'save the mobile number'in query:
            speak("ok sir")
            speak("let me prepare my self")
            speak("and the system")
            option= webdriver.ChromeOptions()
            option.headless = True
            driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
            driver.maximize_window()
            skdj='https://contacts.google.com/'
            driver.get(skdj)
            sleep(3)
            driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("xpredator2021@gmail.com")
            pyautogui.hotkey('enter')
            sleep(3)
            driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Sparsh9803")
            pyautogui.hotkey('enter')
            sleep(3)
            skdj='https://contacts.google.com/'
            driver.get(skdj)
            driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/header/div[4]/div[2]/div/c-wiz/div/div[1]/div/div/div/button/span[3]').click()
            driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/header/div[4]/div[2]/c-wiz/div[1]/div[1]/div/div/div/button/span[3]').click()
            sleep(3)
            speak("what is the first name of the person, sir")
            inks=takecommand()
            driver.find_element(By.XPATH,'/html/body/div[7]/c-wiz[2]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input').send_keys(inks)
            speak("what is the surname of the person, sir")
            klsi=takecommand()
            driver.find_element(By.XPATH,'/html/body/div[7]/c-wiz[5]/div/div[1]/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/input').send_keys(klsi)
            speak("sir do you want me to save his email address also in his contect detail")
            eml=takecommand()
            if'yes'in eml:
                speak("ok sir then tell me what is the email address of the person")
                ssdfs=takecommand()
                driver.find_element(By.XPATH,'/html/body/div[7]/c-wiz[5]/div/div[1]/div[2]/div/div/div[5]/div/div/div[2]/div[1]/div[1]/div/div[1]/input').send_keys(ssdfs)
            elif 'no'   in eml:
                speak("ok sir")
            else:
                speak("ok sir")
            speak("now sir tell me the phone number ")
            kkxi=takecommand()
            driver.find_element(By.XPATH,'/html/body/div[7]/c-wiz[5]/div/div[1]/div[2]/div/div/div[6]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input').send_keys(kkxi)
            speak("ok sir i got all information")
            driver.find_element(By.XPATH,'/html/body/div[7]/c-wiz[5]/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[2]/button/span').click()
            speak("and the number has been successfully save on your google contect")
            speak("anything else sir")
            
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
            
        elif'dido'in query or 'play dido'in query or 'play thank you'in query:
            speak("ok sir,")
            speak("task has been done")
            webbrowser.open("https://www.youtube.com/watch?v=qz59IsgjUlc")
        
        elif'thomas'in query:
            speak("hmm")
            sdfsdf= "C:\\Users\\Manav sharma\\sparsh\\.vscode\\main\\114F23BA0F0FE89F431D3F0E76C53089_video_dashinit.mp4"
            os.startfile(sdfsdf)
        
        elif'another women'in query:
            speak("another women sir")
            sladfjd="C:\\Users\\Manav sharma\\sparsh\\.vscode\\main\\another women.mp4"
            os.startfile(sladfjd)
        
        elif'who is men'in query or 'who is man'in query:
            speak("men are those who know ")
            speak("how to fight, get sun on skin,, eat meat, explore the unkown, lift heavy,put your body on the line, put money on the line, enter fight or flight mode, puke on the led day, approach women unprepared")
        
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
                print("it's eveining sir")
                speak("it's eveining sir")
        
        elif'that nice' in query or 'well done' in query:
            speak("thank you sir")

        elif'shelby style'in query or 'style'in query:
            speak("perfect")
            codePath = "C:\\Users\\Manav sharma\\sparsh\\.vscode\\main\\thomas shelby.mp4"
            os.startfile(codePath)
        
        elif'make a note'in query or 'write this down' in query or 'or remember this' in query:
            speak("ok sir wait let me open up my notepad")
            pyautogui.hotkey("win")
            pyautogui.hotkey("n")
            pyautogui.hotkey("o")
            pyautogui.hotkey("t")
            pyautogui.hotkey("e")
            pyautogui.hotkey("p")
            pyautogui.hotkey("a")
            pyautogui.hotkey("d")
            pyautogui.hotkey("enter")
            speak("ok sir now tell me what do you want me to write")
            note=takecommand()
            pyautogui.hotkey(note)

        elif'excel'in query or 'sheet'in query:
            speak("ok sir tell me")
            speak("which excal sheet do you need")
            speak("new one or save one")
            ion=takecommand
            if 'new'in ion :
                speak("ok sir")
                speak("let me open up you a new excel sheet")
                pyautogui.hotkey("win")
                pyautogui.hotkey(".")
                pyautogui.hotkey("e")
                pyautogui.hotkey("x")
                pyautogui.hotkey("c")
                pyautogui.hotkey("e")
                pyautogui.hotkey("l")
                pyautogui.hotkey("enter")
                sleep("2")
                pyautogui.hotkey("enter")
            elif'save'in ion:
                speak("ok sir tell me what is the name of the file")
                
        elif'hindi mood'in query:
            speak("playing hindi song for you ")
        
        elif 'hell no 'in query:
            speak("what happend sir")
        
        elif'board' in query :
            speak("don't ware sir ")
            speak("i have an idea ")
            speak("can i share it with you ")
            dkt= takecommand()
            if 'what it is' in dkt or 'yes' in dkt:
                speak("let's play some game")
                speak("and listion some song")
                speak("do you like it ")
                dlk=takecommand()
                if'fuck you' in dlk or 'no' in dlk:
                    speak("ok sir")
                elif'yes'in dlk or 'it is good':
                    speak("k sir i am playing game or song for you ")
                    cp=''
                    os.startfile()
                    
            elif 'no' in dkt:
                speak("no problem sir")

        elif'what are you doing'in query:
            speak("nothing much sir")
            speak("i am reading a new article")
            speak("and gathuring some information for you sir")
            speak("can i tell you ")
            speak("what was i read")
            idn=takecommand()
            if 'yes'in query:
                speak("that's nice of you sir")
                speak("ok ")
                speak("i read about")
                driver.maximize_window()
                url  = 'https://www.google.com/search?q=new+technology+news&sxsrf=AJOqlzWMiasvZOsY9t4lGo9yy3BS_b9WSA:1674242359753&source=lnms&tbm=nws&sa=X&ved=2ahUKEwi6zPvo7tb8AhXm9zgGHdDeALAQ_AUoAXoECAEQAw&biw=1536&bih=718&dpr=1.25'
                driver.get(url)
            else:
                speak("no problem sir ")
        
       
        elif'mom want to talk'in query or 'mom talk'in query or 'mom'in query:
            speak("yes MOM ")
            speak("do you need any help")

        elif'ford'in query:
            speak("ok sir")
            dlskf="C:\\Users\\Manav sharma\\sparsh\\.vscode\\main\\ford vs fa.mp4"
            
        elif'eat somethnig'in query:
            speak("i am already eating sir")
        
        elif'battery'in query or 'how much battery'in query or 'battery life'in query or 'power'in query:
            speak("ok sir let me check ")
            speak("accound to the statics")
            print("Battery percentage : ", battery.percent)
            speak(f"the battery percentage is {battery.percent}")
            print("Power plugged in : ", battery.power_plugged)
            speak(f"the power plugged in{battery.power_plugged}")
            print("Battery left : ", convertTime(battery.secsleft))
            speak(f"battery left: {convertTime(battery.secsleft)}")
            
#   this is for instagram message 
        elif'message on instagram'in query or 'message'in query:
            speak("whom you want to send the message sir")
            into=takecommand()
            if'manav'in into or 'manav bhai' in into :
                speak(" ok sir")
                speak("wait a sec let me open up the window")
                speak("what do you want to tell manav bhi, sir")
                speak("wait a minute sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                tin='https://www.instagram.com/direct/t/340282366841710300949128176034922014222'
                driver.get(tin)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'Nikhil ITI' in into:
                speak(" ok sir")
                speak("what do you want to tell Nikil Yadav, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                ti='https://www.instagram.com/direct/t/340282366841710300949128227293546442947'
                driver.get(ti)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                pyautogui.hotkey("enter")
                speak("the message is send successfully sir")
                driver.close()
            elif'Prem' in into:
                speak(" ok sir")
                speak("what do you want to tell Prem, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128233352981759398'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                pyautogui.hotkey("enter")
                speak("the message is send successfully sir")
                driver.close()
            elif'Rachit' in into or 'ray' in into:
                speak(" ok sir")
                speak("what do you want to tell rachit, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iip='https://www.instagram.com/direct/t/340282366841710300949128222845215451429'
                driver.get(iip)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'Yashpal'in into or 'yash pal'in into or 'fauji'in into:
                speak(" ok sir")
                speak("what do you want to tell yashpal, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128256207608886026'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'harsh'in into or 'ghoda' in into or 'solanki' in into:
                speak(" ok sir")
                speak("what do you want to tell harsh, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128334123308601880'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'anuj bhai'in into:
                speak(" ok sir")
                speak("what do you want to tell anuj, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128220149931552496'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'mota bhai'in into or 'manish bhai' in into or 'thakur'in into:
                speak(" ok sir")
                speak("what do you want to tell manish, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128222216457490074'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'suar'in into or 'mr pig' in into or 'shivam'in into:
                speak(" ok sir")
                speak("what do you want to tell shivam, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128167360191469222'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'paawan'in into or 'singh sahab'in into :
                speak(" ok sir")
                speak("what do you want to tell paawan, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128459935766506165'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'tushar'in into:
                speak(" ok sir")
                speak("what do you want to tell tushar, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128147195487207266'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'abhishek bhai' in into or'abhi bhiya'in into:
                speak(" ok sir")
                speak("what do you want to tell abhishek bhaiya, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128226562824409029'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'gulzaar'in into or 'gulnaaz'in into :
                speak(" ok sir")
                speak("what do you want to tell gulnaaz, sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128300500184705194'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'karuna'in into or 'kanu'in into :
                speak(" ok sir")
                speak("what do you want to tell karuna , sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128151019819013113'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            elif'ashu bhai'in into or 'ashu' in into or 'ashutosh' in into :
                speak(" ok sir")
                speak("what do you want to tell ashutosh bhaiya , sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128247195750013994'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()
            
            elif'Anjali' in into :
                speak(" ok sir")
                speak("what do you want to tell anjali , sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128231597370492756'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                pyautogui.hotkey("enter")
                speak("the message is send successfully sir")
                driver.close()

            elif'tannu' in into:
                speak(" ok sir")
                speak("what do you want to tell tarannum , sir")
                ent=takecommand()
                option= webdriver.ChromeOptions()
                option.headless = True
                driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
                driver.maximize_window()
                instagram='https://www.instagram.com/'
                driver.get(instagram)
                sleep(3)
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("sparsh.comm")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Ammsh8060@")
                driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]').click()
                sleep(4)
                iop='https://www.instagram.com/direct/t/340282366841710300949128208857697691642'
                driver.get(iop)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(ent)
                sleep(3)
                driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                speak("the message is send successfully sir")
                driver.close()


# greading message
        elif'good evening'in query :
            if hour>=18 and hour<20:
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
            else:
                speak("it's not evening sir")
                print("it is not evening sir")
                speak(f"sir the time is {strTime}")
                print(f"sir the time is {strTime}")
                speak("according to the time")                
                print("according to the time")
                if hour>=0 and hour<12:
                    speak("it's morning sir")
                    print("it's morning sir")
                else:
                    speak("it's afternoon sir")
                    print("it's afternoon sir")
# google map  
        elif'google map'in query or 'map'in query or 'go'in query or'route'in query:
            speak("ok sir wait let me open up the web browser")
            speak("now tell me where do you want to go sir")
            location=takecommand()
            option=webdriver.ChromeOptions()
            option.headless = True
            driver = webdriver.Chrome(r'C://Users//Manav sharma//sparsh//.vscode//main//chromedriver_win32//chromedriver.exe')
            driver.maximize_window()
            googlemap='https://www.google.com/maps'
            driver.get(googlemap)
            sleep(2)
            driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]').click()
            driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]').send_keys(location)
            pyautogui.hotkey("enter")
            driver.find_element(By.XPATH,'w/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[4]/div[2]/div[2]/button/span/div').click()
            driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[4]/div[1]/button/span').click()
            driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[4]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/div/div[1]/span[4]/span').click()
            speak("you have to allow google to accese your current location sir")
            speak("pls allow it")
            sleep(5)
            pyautogui.hotkey("enter")
            speak(f"which type of vechice you use to travel to go "+location)
            speak("from car bus or by walk")
            tra=takecommand()
            if 'car'in tra:
                speak("ok sir")
                driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[2]/button/img').click()
            elif'bus'in tra:
                speak("ok sir")
                driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[3]/button').click()
            elif'by walk'in tra:
                speak("ok sir")
                driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[2]/div/div/div/div[4]/button').click()
            else:
                speak("it's not avalable")
            

# song
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

        elif query in GREETINGS:
          speak(random.choice(GREETINGS_RES))
        
        elif 'line' in query:
            speak(random.choice(pkq))
# youtue
        elif'brother youtube'in query:
            speak(f"ok sparsh")
            speak("opening brother youtube chennel")
            webbrowser.open("https://www.youtube.com/@manav_sharma_")
        
        elif'my youtube'in query:
            speak(f"ok sparsh")
            speak("opening your youtube chennel")
            webbrowser.open("https://www.youtube.com/channel/UCv4ExSU-9Ye_xGEcEE8dUNw")
 #  greading
        elif'hello' in query:
            speak(random.choice(GREETINGS_RES))
# open application
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
        
        elif'my requirement' in query:
            speak("to get a best performence")
            speak("we want")
            speak("")

        elif'refresh the page' in query or ' refresh'in query:
            pyautogui.hotkey('f5')
            speak("refresh has been done")

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
        
        elif'give me the weather detail'in query or 'weather detail' in query or'today weather'in query:
            speak("ok sir, let me check for you")
            speak("according to google sir")

                 
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
# search in application
        elif'youtube' in query:
           Query = query.replace("ather ", "")
           QUERY = Query.replace("youtube search","")
           from youtube import YouTubeSearch
           YouTubeSearch(query)
        
        elif'google' in query:
           import wikipedia as googleScrap
           query = query.replace("ather ","")
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
        
        elif'peaky blinder'in query or 'peaky blinder quote'in query or'peaky blinder word'in query or 'today quote'in query:
            speak("ok sir")
            speak("i have a best quote for you")
            speak(random.choice(pkq))
                 
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
           speak("my name is arther ")
           speak("and i know your name")
           speak(f"your name is sparsh ")
        
        elif'say hello'in query or 'say hi'in query:
            query = query.replace("ather ","")
            query = query.replace("say hello","")
            query = query.replace("say hi","")
            speak(f"hello"+query)
            speak("how are you")
            inw=takecommand()
            if 'fine' in inw or 'good'in inw:
                speak("nice to hear that")
                speak("hope your day will fine")
            
            elif'not good'in inw or 'not'in inw :
                speak("no problem")
                speak("i will help you")

        elif'wake up'in query:
            speak("i am up sir")
            speak("tell me how can i help you, sir")
        
        elif'my self'in query or 'who is sparsh'in query:
            speak("your name is sparsh sharma")
            speak("his father name is MR. Arun kumar sharma ")
            speak("he is genius")
            speak("he make website like black devil .com")
            speak("there is a lot of inovetion he do like creating me ")
            speak("he is my master, friend and a good partner")

        elif 'are you there 'in query:
            speak("at your service sir")
            speak("what can i do for you ")
#  new project       
        elif'new project' in query:
            speak("ok sir let me prepare system sir")
            codePath='C:\\Users\\Manav sharma\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(codePath)
            speak("do you want to save this file sir")
            ye=takecommand()
            if 'yes' in ye:
                speak("is that a python file sir")
                speak("or same thing else sir ")
                yt=takecommand()
                if 'python'in yt:
                    speak("ok sir, now tell me sir which name do you want to save this file")
                    ii=pyautogui.__file__
                    go=takecommand()
                    name4=f"{go}.py"
                    ii.save(name4)
                    speak("the file has been save sir")
                elif'c'in yt or 'c plus plus ' in yt:
                    speak("ok sir, now tell me sir which name do you want to save this file")
                    eeeeeeee=pyautogui.__file__
                    re=takecommand()
                    uiuio=f"{re}.c"
                    eeeeeeee.save(uiuio)
                    speak("the file has been save sir")
                else:
                    speak("i can't do this sir right now")
                    speak("please tell me something else ")
                
            elif'no'in ye:
                speak("ok sir")
                speak("but if you don't want to save the file")
                speak("your work and time will be wasted sir")
            
        elif'no problem'in query:
            speak("ok sir")
            speak("as you wish")

        elif'introduce yourself'in query:
           speak(f"ok sparsh")
           speak("my name is ather  ,I am a A.I which is able to perform task like chat bot, etc. It provides basic functionality for any assistant application. It is based on artificial intelligence, It is also powerful like JARVIS")
        
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
           
        # elif 'take screenshot' in query or "take a screenshot" in query or 'capture the screen'in query or 'take a ss'in query or 'take ss' in query:
        #     speak("by what name do you want me to save the screenshot?")
        #     name = takecommand()
        #     speak(f"alrightsparsh, taking the screen shot")
        #     img = pyautogui.screenshot()
        #     name2 = f"{name}.png"
        #     img.save(name2)
        #     speak("The screenshot has been succesfully captured")
        elif 'take screenshot' in query or "screenshot" in query or  'take a screenshot'in query :
            speak("ok sir taking Screen Shot")
            pyautogui.press("window")
            pyautogui.press("prt sc")

        # elif'camera' in query or "video storage" in query or 'gallery'in query:
        #     speak("ok sir")
        #     speak("opening gallery ")
        #     os.open(codepath)
        
        elif 'click the photo'in query or 'photo' in query or 'click'in query:
            speak("ok sir")
            speak("let me open up the camera")
            pyautogui.hotkey("win")
            pyautogui.hotkey(".")
            pyautogui.hotkey("c")
            pyautogui.hotkey("a")
            pyautogui.hotkey("m")
            pyautogui.hotkey("e")
            pyautogui.hotkey("r")
            pyautogui.hotkey("a")
            pyautogui.hotkey("enter")
            speak("say chees")
            speak("1")
            speak("2")
            speak("3")
            pyautogui.hotkey("space"or"enter")
            speak("the photo has been clicked")
            speak("it's save in your gallery")



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
            rrr=r*rr
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
                    Query = query.replace("ather ", "")
                    QUERY = Query.replace("youtube search","")
                    from youtube import YouTubeSearch
                    YouTubeSearch(query)
                elif "google" in xx:
                   query = query.replace("ather ","")
                   query = query.replace("google search","")
                   query = query.replace("google","")
                   speak(f"this is what i found on the websparsh")
                   pywhatkit.search(query) 

# # face_recognition
# recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
# recognizer.read('trainer/trainer.yml')   #load trained model
# cascadePath = "haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

# font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


# id = 2 #number of persons you want to Recognize


# names = ['','sparsh sharma'
#         '1','papa ji']  #names, leave first empty bcz counter starts from 0



# cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
# cam.set(3, 640) # set video FrameWidht
# cam.set(4, 480) # set video FrameHeight

# # Define min window size to be recognized as a face
# minW = 0.1*cam.get(5)
# minH = 0.1*cam.get(6)

# # flag = True

# while True:

#     ret, img =cam.read() #read the frames using the above created object

#     converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

#     faces = faceCascade.detectMultiScale( 
#         converted_image,
#         scaleFactor = 1.2,
#         minNeighbors = 5,
#         minSize = (int(minW), int(minH)),
#        )

#     for(x,y,w,h) in faces:

#         cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

#         id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

#         # Check if accuracy is less them 100 ==> "0" is perfect match 
#         if (accuracy < 100):
#             id = names[id]
#             ts()
#             accuracy = "  {0}%".format(round(100 - accuracy))
            
            


#         else:
#             id = "unknown"
#             accuracy = "  {0}%".format(round(100 - accuracy))
#             speak("you are not sparsh")
#             exit()
        
#         cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
#         cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  


    
#     cv2.imshow('camera',img) 

#     k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
#     if k == 27:
#         break

# # Do a bit of cleanup
# print("verified ")
# cam.release()
# cv2.destroyAllWindows()
