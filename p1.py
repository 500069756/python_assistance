import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evenning!")
    speak("I am zira the voice assistant. how may i help you?")
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e :
        print(e)

        print("say that again")
        return "none"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('500069756@stu.upes.ac.in', '*******')
    server.sendmail('500069756@stu.upes.ac.in', to, content)
    server.close()
    
              

if __name__ == "__main__":
    wishME()
    while True:
        query =takeCommand().lower()
    #logic for
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H: %M:%S")
            speak(f"dear user, the time is {strtime}")

        elif 'open visual' in query:
            codepath ="C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codepath)
       
        elif 'email to himani' in query:
             
             try:
                 speak("what should i say?")
                 content = takeCommand()
                 to = "bansal.himani820@gmail.com"
                 sendEmail(to,content)
                 speak("email has been sent1")
             except Exception as e :
                 print(e)
                 speak("sorry cant send this email")


        elif 'play music' in query:
            music_dir= "C:\\Users\\hp\\music"
            songs=os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play video' in query:
            video="C:\\Users\\hp\\Videos\\Captures"
            videos=os.listdir(video)
            a=int(input("enter no."))
            os.startfile(os.path.join(video, videos[a]))



        
