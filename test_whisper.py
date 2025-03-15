import whisper

def test_whisper():
    # Load model
    model = whisper.load_model("base")
    
    # Transcribe audio
    result = model.transcribe("audio.mp3")
    
    # Print transcription
    print(result["text"])

if __name__ == "__main__":
    test_whisper()
