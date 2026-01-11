# Description
CLI for voice cloning using the ElevenLabs AI service.

# How to use
## In docker
### Clone voice
- put `voices/voice.mp3`
- execute:
```shell
docker run \ 
  -e ELEVENLABS_TOKEN=sk_... \
  -v $(pwd)/voices:/app/src/voices \
  deusalex/voice-cloner-cli:latest cli clone-voice --name "My self voice"
```
- copy `<voice_id>` from the command output

### Make TTS
- execute:
```shell
docker run \ 
  -e ELEVENLABS_TOKEN=sk_... \
  -v $(pwd)/audios:/app/src/audios \
  deusalex/voice-cloner-cli:latest cli make-tts --voice-id <voice_id> --text "My test for speach"
```
- see a file at `audios/` folder

## At local
### Clone
```shell
git clone https://github.com/alex-deus/voice-cloner.git
cd voice-cloner
```

### Install
```shell
pip install poetry
poetry install --no-root
```

### Configure
```shell
export ELEVENLABS_TOKEN="sk_..."
```

### Clone voice
- put `voices/voice.mp3`
- execute: `poetry run ./cli.py clone-voice --name "My self voice"`
- copy `<voice_id>` from the command output

### Make TTS
- execute: `poetry run ./cli.py make-tts --voice-id <voice_id> --text "My test for speach"`
- see a file at `audios/` folder

# License
MIT License - see LICENSE file for details.
