import whisper

model = whisper.load_model("base", device="cuda")
result = model.transcribe(r"tmp\\output.wav")
print(result["text"])
