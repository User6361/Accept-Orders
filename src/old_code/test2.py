import speech_recognition as sr

recognizer = sr.Recognizer()

def get_voice_input():
    with sr.Microphone() as source:
        print("This is you phone number")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("You say ", text)

        return text
    except sr.UnknownValueError:
        print("Sorry, speech recognition was not possible")
        return ""
    except sr.RequestError as e:
        print("Error when requesting Google Speech Recognition service:", e)
        return ""


