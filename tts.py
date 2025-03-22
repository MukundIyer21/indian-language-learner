import whisper
model = whisper.load_model("medium")
transcribe = model.transcribe('test.mp3')
print(transcribe.text)