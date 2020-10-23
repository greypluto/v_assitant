import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning !")
    elif(hour>=12 and hour<18):
        speak("Good afternoon !")
    else:
        speak("Good night !")

    speak("I'm  zero one. tell me how may i help you sir??")    

def takecommand():
    r= sr.Recognizer() 
    with sr.Microphone() as source:
     print(" Listening.....")
     r.pause_threshold=1
     audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said: {query} \n")
    except Exception as e:
        print(" Say that Again please....")
        return "None"
    return query

def send_sms(message,number):
    # i have used fast2smsm API for sending SMS
        url= "https://www.fast2sms.com/dev/bulk"
        para={
                "authorization":" ", 
                "sender_id":"",
                "message":message,
                "language":"english",
                "route":"p",
                "numbers":number
        }
        response=requests.get(url,params=para)
        dic=response.json()
        print(dic)

if __name__ == "__main__":
 
    di= {"name":"phone number","name":"phone number"}
    greet()
    while(True):
        query=takecommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...") 
            query= query.replace("wikipedia", "")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "google" in query:
          
            webbrowser.open("google.com")

        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "instagram" in query:
            webbrowser.open("instagram.com")

        elif "amazon" in query:
            webbrowser.open("amazon.in")
        elif "sms" in query:
            speak("whom would you like to send sms to ?")
            print("whom would you like to send sms to ?")
            query=takecommand().lower()
            de=query
            ph=di.get(de)
            speak("what message would like to send?")
            print("what message would like to send?")
            query=takecommand().lower()
            ms=query
            send_sms(ms,ph)