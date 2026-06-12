import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# We import our "speech recognition" module we installed
# Then we create a "recognizer", so we can recognize our voice
# also don't forget to always install pipwin, then install pyaudio with "pipwin install pyaudio" to avoid errors

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
    elif 'should' in command:
        if 'i' in command:
            searchUp = 'Should I pay my taxes??'
            pywhatkit.search(searchUp)
        if 'you' in command:
            searchUp = 'Should I pay my taxes???'
    elif 'search up' in command:
        searchUp = command
        pywhatkit.search(searchUp)


run_jarvis()

