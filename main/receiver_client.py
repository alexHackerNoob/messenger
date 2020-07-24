import requests
import time
from messages import format_message

after = time.time() - 24 * 60 * 60
while True:

    response = requests.get('http://127.0.0.1:5000/messages', params = {'after': after})
    messages = response.json()['messages']
    for message in messages:
        print(format_message(message))
        after = message['time']
    time.sleep(1)