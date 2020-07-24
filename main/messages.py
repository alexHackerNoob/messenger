import time
from datetime import datetime

stored_messages = [
    {'name': 'Jack', 'time': time.time(), 'text': '1'},
    {'name': 'Jack', 'time': time.time(), 'text': '2'},
]

def filter_stored_messages(stored_messages, key, min_time):
    new_stored_messages = []
    for message in stored_messages:
        if message[key] > min_time:
            new_stored_messages.append(message)
    return new_stored_messages

def format_message(message):
    name = message['name']
    text = message['text']
    dt = datetime.fromtimestamp(message['time'])
    dt_beauty = dt.strftime('%Y/%m/%d %H:%M:%S')
    return f'{name} {dt_beauty}\n {text}\n'