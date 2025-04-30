# analysis/keyword_detector.py

def find_keywords(transcript, keywords):
    # Mock version: returns fixed times for demo/testing
    # You'd normally search for keywords and map them to real timestamps
    detected = {}
    lower_text = transcript.lower()

    for keyword in keywords:
        if keyword in lower_text:
            # Mock: Assume keyword appears around minute marks
            if keyword == "unbox":
                detected["unboxing"] = 60  # e.g., at 1:00 min
            elif keyword == "feature":
                detected["feature_demo"] = 180  # e.g., at 3:00 min
            elif keyword == "verdict":
                detected["final_verdict"] = 300  # e.g., at 5:00 min

    return detected
