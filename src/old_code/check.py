import speech_recognition as sr
import time
import random
from playsound import playsound

path_check = "C:\\Users\\Admin\\Desktop\\python_IDEA\\project\\src\\alexa\\check\\"
sounds_check = ['check1', 'check2']


def listen_to_check():
    recognizer = sr.Recognizer()

    start_time = time.time()
    timeout_seconds = 10

    while True:

        current_time = time.time()

        if current_time - start_time > timeout_seconds:
            print("Время выполнения цикла превышено")
            break
        time.sleep(1)

        with sr.Microphone() as source:

            play_check = str(path_check) + str(random.choice(sounds_check)) + ".mp3"
            playsound(play_check)

            print("Это ваш номер телефона?")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            if text == "да":
                print("Я ВАС ПОНЯЛА!!!")
                break
            elif text == "нет":
                print("ДИКТУЙТЕ ЕЩЕ РАЗ!!")
                break
            else:
                print("Я ВАС НЕ ПОНЯЛА")

        except sr.UnknownValueError:
            print("Извините, не удалось распознать речь.")

        except sr.RequestError as e:
            print("Ошибка при запросе к сервису Google Speech Recognition:", e)
