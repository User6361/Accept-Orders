import speech_recognition as sr
import time
import random
from playsound import playsound

path_check = "path to check"
sounds_check = ['check1', 'check2']


def listen_to_check():
    recognizer = sr.Recognizer()

    start_time = time.time()
    timeout_seconds = 10

    while True:

        current_time = time.time()

        if current_time - start_time > timeout_seconds:
            print("Time out!")
            break
        time.sleep(1)

        with sr.Microphone() as source:

            play_check = str(path_check) + str(random.choice(sounds_check)) + ".mp3"
            playsound(play_check)

            print("This is your phone number?")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            if text == "да":
                print("Ok")
                break
            elif text == "нет":
                print("Say again")
                break
            else:
                print("I don't understand you")

        except sr.UnknownValueError:
            print("Sorry, speech recognition was not possible.")

        except sr.RequestError as e:
            print("Error when requesting Google Speech Recognition service:", e)
