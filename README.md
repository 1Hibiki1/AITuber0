# AITuber

## Prereqs

You'll have to install the following:

* [Python](https://www.python.org/downloads/) (make sure to add this to PATH)
* [Node JS](https://nodejs.org/en/download/current/) (make sure to add this to PATH)
* [VTube Studio](https://store.steampowered.com/app/1325860/VTube_Studio/)
* [VOICEVOX](https://voicevox.hiroshiba.jp/)
* [VB-CABLE](https://vb-audio.com/Cable/)
* [OBS studio](https://obsproject.com/)

Make sure python and node works by opening a terminal (powershell!!) and executing `python` and `node`. Then, clone this repo and open a terminal in its directory. If windows ever asks for firewall permissions or whatever in any of the steps, allow everything.

## Check if tts works

1. Open VOICEVOX. Accept TOS and stuff
2. `cd` into VVOX in the terminal u opened and execute the following commands:

```console
pip install -r requirements.txt
python AI.py
```

Now you should see a prompt. Type something in Japanese and press enter. After some time you should hear the tts result being played. Congrats, tts works! Exit out by typing 'q'.

## Check if character AI works

1. `cd` into charai and execute the following:

```console
npm i
node index.js
```

2. If everything goes fine, you should see a prompt. Don't type anything yet.
3. Open a new terminal and `cd` into VVOX again.
4. Run the server with `python server.py 6969`.
5. Go back the node terminal and type some message in Japanese. You will see the response printed on the terminal after some time. If you now go back to the python terminal, you should see a "Got text", and after some time it should generate the voice and play it.

## Setup VTube Studio

Meh, this is kinda involved and ill fill this out later. lemme know if you got everything else working
