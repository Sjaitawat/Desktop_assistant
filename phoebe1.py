import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import random



engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !!")    
    else:
        speak("Good Evening !!")
    speak("Hey I am Phoebe, How may I help you?")        

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')    
        print(f"User said: {query}\n")  

    except Exception as e :
        print("say that again please ...")
        return "none"
    return query       

def sendEmail(to,content) :
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com','password')
    server.sendmail('email@gmail.com',to,content)
    server.close()    

def show(query):
    
    if 'friends' in query:
        dr ="path"
        episode= os.listdir(dr)
        os.startfile(os.path.join(dr,(episode[0]))) 
    elif 'Harry potter' in query:
        dr ="path"
        episode= os.listdir(dr)
        os.startfile(os.path.join(dr,(episode[0]))) 


if __name__=="__main__":
    wishMe()
    while True:
     query = takecommand().lower()
    
     if 'wikipedia' in query:
        speak('Searching wikipedia.....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences=2)
        speak('According to wikipedia...')
        print(results)
        speak(results)

     elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
     elif 'open google' in query:
        webbrowser.open("google.com")

     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")  

     elif 'play music' in query:
         music_dr ="C:\\Users\\soumy\\Music"
         songs= os.listdir(music_dr)
         print(songs)
         n=random.randint(0,len(songs))
         os.startfile(os.path.join(music_dr,(songs[n])))

     elif 'time' in query:
         strtime= datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Ma'am the time is {strtime}")   

     elif 'open code' in query:
         codepath = "C:\\path"  
         os.startfile(codepath) 
             
     elif 'email' in query:
         try:
             speak("What should it say?")
             content = takecommand()
             to = "email@gmail.com"
             sendEmail(to,content)
             speak("Email has been sent")
         except Exception as e:
            print(e)
            speak("Sorry am  unable to do that")   

     elif 'tell me a joke' in query:
         joke_list = ['I ate a clock yesterday, it was very time-consuming.','Have you played the updated kids game? I Spy With My Little Eye . . . Phone.','A perfectionist walked into a bar...apparently, the bar wasn’t set high enough','You know it is going to be a bad day when the letters in your alphabet soup spell D-I-S-A-S-T-E-R.','A fire hydrant has H-2-O on the inside and K-9-P on the outside','Did you hear about the crook who stole a calendar? He got twelve months.']
         n=random.randint(0,len(joke_list))
         speak(joke_list[n])

     elif 'good quote' in query:
         quote_list = ['Love For All, Hatred For None','Change the world by being yourself','Every moment is a fresh beginning','Never regret anything that made you smile','Die with memories, not dreams','Aspire to inspire before we expire.' ] 
         n=random.randint(0,len(quote_list))
         speak(quote_list[n])
  
     elif 'show' in query:
         speak('Which one do you want me to open?')
         query=takecommand().lower()
         show(query)
        
     elif 'quit' in query:
        speak('Ok maam ,I am Quiting.....')
        exit()                