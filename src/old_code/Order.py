import speech_recognition as sr
import re
import time
import random
from playsound import playsound

num = []
path_num = "C:\\Users\\Admin\\Desktop\\python_IDEA\\project\\src\\alexa\\num\\"
sounds_num = ['num1', 'num2', 'num3']


def listen_to_num():
    # Создаем объект recognizer
    recognizer = sr.Recognizer()

    start_time = time.time()
    timeout_seconds = 15  # Установите время выполнения в секундах

    while True:

        current_time = time.time()

        if current_time - start_time > timeout_seconds:
            print("Время выполнения цикла превышено")
            break
        time.sleep(1)

        # Определяем источник аудио (микрофон)
        with sr.Microphone() as source:

            play_num = str(path_num) + str(random.choice(sounds_num)) + ".mp3"
            playsound(play_num)
            print("Говорите номер телефона:")
            audio = recognizer.listen(source)

        # Распознаем речь с использованием Google Web Speech API

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            print("Вы сказали:", text)

            # Поиск номера телефона с помощью регулярного выражения
            phone_number = re.search(
                r'(\+?\d{1,2}\s*[-.\s]?)?(\(?\d{3}\)?\s*[-.\s]?)?(\d{3}\s*[-.\s]?\d{2,4})\s*[-.\s]?(\d{2,4})', text)
            if phone_number:
                print("Найден номер телефона:", phone_number.group())
                num.append(phone_number.group())
                print(num[0])
            else:
                print("Номер телефона не найден.")

        except sr.UnknownValueError:
            print("Извините, не удалось распознать речь.")

        except sr.RequestError as e:
            print("Ошибка при запросе к сервису Google Speech Recognition:", e)


    print("GHBDNTTTT")