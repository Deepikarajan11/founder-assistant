mood_log = []

def log_mood(entry):
    mood_log.append(entry)
    return "Mood saved."

def get_mood_history():
    return mood_log[-5:]  # Show last 5 entries
