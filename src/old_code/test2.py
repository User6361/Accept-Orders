import speech_recognition as sr

recognizer = sr.Recognizer()

def get_voice_input():
    with sr.Microphone() as source:
        print("Это ваш номер телефона?")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", text)

        return text
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь.")
        return ""
    except sr.RequestError as e:
        print("Ошибка при запросе к сервису Google Speech Recognition:", e)
        return ""


