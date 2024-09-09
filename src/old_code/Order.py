import speech_recognition as sr
import re
import time
import random
from playsound import playsound

num = []
path_num = "path to nums"
sounds_num = ['num1', 'num2', 'num3']


def listen_to_num():
    # Создаем объект recognizer
    recognizer = sr.Recognizer()

    start_time = time.time()
    timeout_seconds = 15  # Установите время выполнения в секундах

    while True:

        current_time = time.time()

        if current_time - start_time > timeout_seconds:
            print("Time out")
            break
        time.sleep(1)

        # Определяем источник аудио (микрофон)
        with sr.Microphone() as source:

            play_num = str(path_num) + str(random.choice(sounds_num)) + ".mp3"
            playsound(play_num)
            print("Say phone number:")
            audio = recognizer.listen(source)

        # Распознаем речь с использованием Google Web Speech API

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            print("You say ", text)

            # Поиск номера телефона с помощью регулярного выражения
            phone_number = re.search(
                r'(\+?\d{1,2}\s*[-.\s]?)?(\(?\d{3}\)?\s*[-.\s]?)?(\d{3}\s*[-.\s]?\d{2,4})\s*[-.\s]?(\d{2,4})', text)
            if phone_number:
                print("Phone number is found: ", phone_number.group())
                num.append(phone_number.group())
                print(num[0])
            else:
                print("Phone number is not found")

        except sr.UnknownValueError:
            print("Sorry, speech recognition was not possible.")

        except sr.RequestError as e:
            print("Error when requesting Google Speech Recognition service:", e)
