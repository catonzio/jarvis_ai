import whisper


class SttComponent:

    def __init__(self):
        self.model = whisper.load_model("base", device="cpu")

    def transcribe(self, audio_path: str) -> dict:
        return self.model.transcribe(audio_path, language="en")
