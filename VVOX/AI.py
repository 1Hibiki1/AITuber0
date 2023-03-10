import urllib
import requests
from playsound import playsound

base_url = "http://localhost:50021"
speech_filename = "sp.wav"
speaker_id = '6'

def speak(sentence):
    # generate initial query
    params_encoded = urllib.parse.urlencode ({'text': sentence, 'speaker': speaker_id})

    r = requests.post (f'{base_url}/audio_query?{params_encoded}')

    voicevox_query = r.json ()
    voicevox_query['volumeScale'] = 4.0
    voicevox_query['intonationScale'] = 1.5
    voicevox_query['prePhonemeLength'] = 1.0
    voicevox_query ['postPhonemeLength'] = 1.0

    # synthesize voice as wav file
    params_encoded = urllib.parse.urlencode({'speaker': speaker_id})
    r = requests.post (f'{base_url}/synthesis?{params_encoded}', json=voicevox_query)

    with open(speech_filename, 'wb') as outfile:
        outfile.write(r.content)

    # play audio file
    playsound(speech_filename)

# while 1:
#     t = input("tts> ")

#     if t == 'q':
#         break
    
#     if t.strip() == "chsp":
#         new_sp = input("enter new speaker> ")
#         speaker_id = new_sp.strip()
#         continue

#     speak(t)
