import urllib
import requests

import platform
cur_OS = platform.system()

# import playsound if not on windows
if cur_OS == "Windows":
    import winsound
else:
    from playsound import playsound

# VOICEVOX engine server url
base_url = "http://localhost:50021"

# audio file to save generated voice in
speech_filename = "sp.wav"

# voice bank ID
speaker_id = '1'

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
    if cur_OS == "Windows":
        winsound.PlaySound(speech_filename, winsound.SND_FILENAME)
    else:
        playsound(speech_filename)


if __name__ == '__main__':
    print("type 'q' to exit! :)\n")
    
    while 1:
        t = input("tts> ")

        if t == 'q':
            break
        
        if t.strip() == "chsp":
            new_sp = input("enter new speaker> ")
            speaker_id = new_sp.strip()
            continue

        speak(t)
