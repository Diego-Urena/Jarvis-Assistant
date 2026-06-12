import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            text = 'JARVIS ACTIVATED'
            talk(text)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    searchUp = ''
    if 'play' in command:
        if 'my playlist' not in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'my playlist' in command:
            talk('playing your playlist')
            playlist = 'https://www.youtube.com/playlist?list=PLY5ml3SW1L_DXI329SRPWKOu47PUxaGxX'
            pywhatkit.playonyt(playlist)
    elif 'what' in command:
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('The current time is ' + time)
        elif 'is' in command:
            searchUp = command.replace('what is', '')
            whatInfo = wikipedia.summary(searchUp, 1)
            print(whatInfo)
            talk(whatInfo)
    elif 'search up' in command:
        searchUp = command.replace('what is' , '')
        pywhatkit.search(searchUp)


run_jarvis()

