import speech_recognition as sr

recognizer = sr.Recognizer()

phone_numbers = []


def add_phone_number(number):
    phone_numbers.append(number)
    print("Number is added", number)


def listen_to_num():
    with sr.Microphone() as source:
        print("Say current phone number")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("You say ", text)

        import re

        phone_number = re.search(
            r'(\+?\d{1,2}\s*[-\.\s]?)?(\(?\d{3}\)?\s*[-\.\s]?)?(\d{3}\s*[-\.\s]?\d{2,4})\s*[-\.\s]?(\d{2,4})', text)
        if phone_number:
            phone_number = phone_number.group()
            print(phone_number)
            add_phone_number(phone_number)

        else:
            print("NUmber is not found")
    except sr.UnknownValueError:
        print("I dont understand audio")
    except sr.RequestError as e:
        print("Error when accessing the Google Speech Recognition service:", e)

    print("Phones numbers ", phone_numbers)
