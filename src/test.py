import speech_recognition as sr

recognizer = sr.Recognizer()

phone_numbers = []


def add_phone_number(number):
    phone_numbers.append(number)
    print("Номер телефона добавлен:", number)


def listen_to_num():
    with sr.Microphone() as source:
        print("Скажите номер телефона:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали:", text)

        import re

        phone_number = re.search(
            r'(\+?\d{1,2}\s*[-\.\s]?)?(\(?\d{3}\)?\s*[-\.\s]?)?(\d{3}\s*[-\.\s]?\d{2,4})\s*[-\.\s]?(\d{2,4})', text)
        if phone_number:
            phone_number = phone_number.group()
            print(phone_number)
            add_phone_number(phone_number)

        else:
            print("Номер телефона не найден.")
    except sr.UnknownValueError:
        print("Извините, не удалось распознать речь.")
    except sr.RequestError as e:
        print("Ошибка при запросе к сервису Google Speech Recognition:", e)

    print("Массив номеров телефонов:", phone_numbers)
