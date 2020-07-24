import time
from datetime import datetime
def getCurrentFormattedTime():
    now = datetime.now()
    return now.strftime("%d/%m/%y %I:%M")

def getCurrentUnformattedTime():
    return time.time()