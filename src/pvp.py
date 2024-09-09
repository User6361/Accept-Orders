import random
import json
import test
import pyaudio
from vosk import Model, KaldiRecognizer
from playsound import playsound


path_by = "Paths"
path_check = "to"
path_more = "mp3"
path_base = "files"
path_er = "!"

sounds_by = ['by1', 'by2', 'by3', 'by4']
sounds_check = ['check1', 'check2']
sounds_more = ['more1', 'more2']
sounds_base = ['base1', 'base2', 'base3']
sounds_er = ['er1', 'er2']

with open("lib.json", "r", encoding="UTF=8") as f:
    lib_file = json.load(f)

model = Model("model2")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

time_list = []


def main():
    print("''''''''''''''''''''''''''''''")
    print("$!$!$!$!__Alexa_1.2__$!$!$!!$!")
    print("''''''''''''''''''''''''''''''")

    playsound("path to playsound file")
    time_list.clear()

    def listen():
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            time_list.append(1)
            if len(time_list) > 38:
                break
            if (rec.AcceptWaveform(data)) and (len(data) > 0):
                answer = json.loads(rec.Result())
                if answer['text']:
                    yield answer['text']

    for text in listen():

        if text in lib_file["Order"]:
            test.listen_to_num()
            var = test.phone_numbers[0]
            print(var)
            time_list.clear()
            break

        if text in lib_file["By"]:
            play_by = str(path_by) + str(random.choice(sounds_by)) + ".mp3"
            playsound(play_by)
            time_list.clear()
            break
        if text not in lib_file["By"] and text not in lib_file["Order"]:
            playsound("error_word.mp3")
            time_list.clear()

#num.listen_to_num возврашает номер телефона сказанным пользователем
# следущая задача прочесть по базам данных данный номер телефона и проверить заказы
# с помощью кода назвать ближайшие заказы или их отсутви
