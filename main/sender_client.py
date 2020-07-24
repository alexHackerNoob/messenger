import requests

name = input("name: ")
password = input("password: ")
while True:
    text = input("text: ")
    message = {'name': name, 'text': text, 'password': password}
    response = requests.post('http://127.0.0.1:5000/send', json = message)
    if response.status_code == 401:
        name = input("name: ")
        password = input("password: ")

