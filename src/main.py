import pvporcupine
import struct
import pyaudio
import pvp

porcupine = None
pa = None
audio_stream = None
print("Listeting...")

try:
    access_key = "4JZPO8wujsl/3LKnOsNZdw5kADpI9QSqWoOioYoTwC/qfZUBba9hbQ=="
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=['Alexa_en_windows_v3_0_0.ppn'])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)
    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keywords_index = porcupine.process(pcm)
        if keywords_index >= 0:
            pvp.main()
            print("Listeting...")
finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.stop_stream()
    if pa is not None:
        pa.terminate()


