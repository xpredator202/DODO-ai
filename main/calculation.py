import pyttsx3
import speech_recognition as sr
import math 

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

while True:
    query = takecommand().lower()

    if 'area of trangle' or 'trangle' in query:
        speak("ok sir tell me the base of the trangle")
        q=takecommand()
        qq=int(q)
        speak("ok now tell me the height of the trangle")
        w=takecommand()
        ww=int(w)
        qw=1/2*q*w
        speak("the area of the trangle is"+qw)

    elif 'area of rectangle' or 'rectangle'in query:
        speak("ok sir tell me the ")