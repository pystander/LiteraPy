# Import libraries 
import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

r = sr.Recognizer()

# Convert audio file (default as .wav)
def convert(path: str, format: str='wav'):
    audio = AudioSegment.from_file(path)
    ext = os.path.splitext(path)[1]
    dest = path.replace(ext, '.' + format)
    audio.export(dest, format=format)
    return dest

# Transcribe .wav audio
def audio_to_text(path: str, lang: str='en-US'):
    file_path = path.replace('wav', '')

    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    audio = AudioSegment.from_wav(path)
    chunks = split_on_silence(audio, min_silence_len=750, silence_thresh=audio.dBFS-16, keep_silence=500)
    full_text = ''

    for i, chunk in enumerate(chunks, start=1):
        chunk_path = os.path.join(file_path, f'chunk{i}.wav')
        chunk.export(chunk_path, format='wav')

        with sr.AudioFile(chunk_path) as src:
            recorded = r.record(src)

            try:
                text = r.recognize_google(recorded, language=lang)
            except sr.UnknownValueError:
                print('(Unrecognized)')
            else:
                text = f'{text.capitalize()}. \n'
                print(text.replace('\n', ''))
                full_text += text

    with open(file_path + 'txt', 'w+') as f:
        f.write(full_text)

    return full_text
