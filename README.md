# Description
CLI for voice cloning using the ElevenLabs AI service.

# How to use
## Install
```shell
pip install poetry
poetry install --no-root
```

## Configure
```shell
export ELEVENLABS_API_KEY="sk_..."
```

## Run
```shell
poetry run ./cli.py clone-voice --file voice.mp3
poetry run ./cli.py make-tts --voice-id <voice_id> --out audio.mp3 --text "My test for speach"
```

# License
MIT License - see LICENSE file for details.
