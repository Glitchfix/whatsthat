import sounddevice as sd
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from qai_hub_models.models.whisper_small_en.model import Whisper
from qai_hub_models.models.whisper_small_en import App as WhisperApp

from qai_hub_models.models._shared.whisper.model import (
    MODEL_ASSET_VERSION,
    MODEL_ID,
    CHUNK_LENGTH,
    SAMPLE_RATE,
)

duration = 10  # in seconds

# Load the Whisper model and tokenizer
whisper = Whisper.from_pretrained(model="small.en")
whisperapp = WhisperApp(whisper)



# Function to process the recorded audio
def process_audio(audio, frames, time, status):
    # Convert the audio to mono
    print(audio.shape)
    # audio = audio[0]
    audio = audio[:, 0]
    # audio, _ = load_demo_audio()
    # Play the audio on the speaker
    sd.play(audio, SAMPLE_RATE)
    sd.wait()
    print(audio.shape)

    transcription = whisperapp.transcribe(audio, SAMPLE_RATE)
    
    print("Transcription:", transcription)

while True:
    # Start recording audio from the microphone
    print("Recording audio...")
    audio = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    print("Audio recorded.")

    # Send the recorded audio to process_audio function
    process_audio(audio, None, None, None)