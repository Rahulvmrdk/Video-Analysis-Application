import whisperx

def find_keywords_with_timestamps(audio_path, keywords, model_size="base"):
    device = "cpu"
    compute_type = "int8"

    # Load model and transcribe
    model = whisperx.load_model(model_size, device, compute_type=compute_type)
    result = model.transcribe(audio_path)

    # Load alignment model
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)

    # Align to get word-level timestamps
    aligned_result = whisperx.align(result["segments"], model_a, metadata, audio_path, device)

    # Extract keywords with timestamps
    detected = {}
    for segment in aligned_result["word_segments"]:
        word = segment["word"].lower()
        for keyword in keywords:
            if keyword in word and keyword not in detected:
                detected[keyword] = segment["start"]
                break

    return detected
