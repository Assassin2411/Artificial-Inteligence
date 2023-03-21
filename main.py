import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import cv2

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    return query

def run_alexa():
    command = listen()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'introduce yourself' in command:
        talk("I am Amit's Alexa, or simply Alexa. I am virtual assistant developed by Amit. I work on the Fire OS 5.0 or higher.")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke()) 
    elif 'open camera' in command:
        cap=cv2.VideoCapture(0)
        while True:
            ret,img=cap.read()
            cv2.imshow('webcam',img)
            cv2.waitKey(10)
            k = cv2.waitkey(10)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
    elif 'stop' in command:
        while True:
            break;    
    else:
        talk('Please say the command again.')


while True:
    run_alexa()