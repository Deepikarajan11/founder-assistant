from datetime import datetime

def get_summary():
    now = datetime.now()
    return f"Today is {now.strftime('%A, %d %B %Y')}. Stay focused and aligned with your goals."
