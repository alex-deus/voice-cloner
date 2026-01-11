#!/usr/bin/env python
import click
from io import BytesIO
from base64 import b64decode

from elevenlabs.client import ElevenLabs


@click.group
@click.option("--api-key", envvar="ELEVENLABS_TOKEN", required=True, help="ElevenLabs API key or set ELEVENLABS_TOKEN")
@click.pass_context
def cli(ctx, api_key: str) -> None:
    ctx.obj = ElevenLabs(api_key=api_key)


@cli.command("clone-voice")
@click.option(
    "--file", "file_path", default="voice.mp3", show_default=True, type=click.Path(exists=True), help="File with voice"
)
@click.option("--name", default="voice", required=True, help="Name for the cloned voice")
@click.pass_obj
def clone_voice(client: ElevenLabs, file_path: str, name: str) -> None:
    with open(file_path, "rb") as f:
        audio_bytes: bytes = f.read()

    voice = client.voices.ivc.create(name=name, files=[BytesIO(audio_bytes)])

    click.echo(f"VoiceID={voice.voice_id} has been created")


@cli.command("make-tts")
@click.option("--voice-id", required=True, help="11labs Voice ID to use")
@click.option(
    "--out", "out_file", default="audio.mp3", show_default=True, type=click.Path(exists=False), help="Output audio file"
)
@click.option("--text", required=True, help="Text to synthesize")
@click.pass_obj
def make_tts(client: ElevenLabs, voice_id: str, out_file: str, text: str) -> None:
    result = client.text_to_speech.convert(
        text=text,
        model_id="eleven_multilingual_v2",
        voice_id=voice_id,
        voice_settings={
            "style": 0,
            "stability": 0.1,
            "similarity_boost": 0.5,
            "use_speaker_boost": False,
        },
    )
    with open(out_file, "wb") as f:
        for b in result:
            f.write(b)

    click.echo(f"Saved to {out_file}")


if __name__ == "__main__":
    cli()