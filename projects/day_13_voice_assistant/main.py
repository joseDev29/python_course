import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes

import webbrowser
import datetime
import wikipedia


voices = {
        'helena': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0',
        'zira': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
}


def get_audio_result():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # delay
        recognizer.pause_threshold = 0.8

        print("Listen")

        audio = recognizer.listen(source)

        try:
            # Search in google
            request = recognizer.recognize_google(audio, language='es-co')
            print('Request: ', request)
            return request
        except sr.UnknownValueError:
            print('Ops!, Unknown value error')
            return 'Ops'
        except sr.RequestError:
            print('Ops!, Request error')
            return 'Ops'


def speak(message: str, voice_id: str):
    # init engine
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.say(message)
    engine.runAndWait()


def request_day():
    today = datetime.date.today()
    week_day = today.weekday()
    week_days = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    speak(f'Hello, today is {week_days[week_day]}', voices['zira'])


def request_hour():
    current_hour = datetime.datetime.now()
    hour_text = f"At this moment it is {current_hour.minute} minutes past {current_hour.hour} o'clock"
    speak(hour_text, voices['zira'])


def greeting():
    current_hour = datetime.datetime.now()
    if current_hour.hour < 6 or current_hour.hour > 20:
        moment = 'Good night'
    elif current_hour.hour >= 6 or current_hour.hour < 13:
        moment = 'Good day'
    else:
        moment = 'Good afternoon'

    speak(f"{moment}, I'm Zira and i'm your personal assistant", voices['zira'])


def main():
    # engine = pyttsx3.init()

    # voices = engine.getProperty('voices')
    # print(type(voices))
    # for voice in voices:
    #     print(voice)

    get_audio_result()
    # speak('Hello world', voices['helena'])
    # greeting()
    # request_day()
    # request_hour()


main()
