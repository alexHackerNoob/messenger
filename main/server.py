from flask import Flask, request, abort
from messages import stored_messages, filter_stored_messages
from time_functions import getCurrentFormattedTime, getCurrentUnformattedTime
app = Flask(__name__)
from users import users

#methods send messages related on user(client)
@app.route("/")
def hello_view():
    return 'Hello, World! <a href="/status">Status</a>'

@app.route("/status")
def status_view():
    return {"status": "Ok",
            "name": "ABC",
            "timeFormatted": getCurrentFormattedTime(),
            "timeUnformatted": getCurrentUnformattedTime()
            }

@app.route("/send", methods=['POST'])
def send_view():
    name = request.json['name']
    password = request.json['password']
    text = request.json['text']
    #TODO validate data

    for token in [name, password, text]:
        if not isinstance(token, str) or not token:# or token > 1024:
            abort(400)

    if name in users:
        if users[name] != password:
            abort(401)#further not executed

    else: #registration
        users[name] = password

    stored_messages.append({'name': name, "text": text, "time": getCurrentUnformattedTime()})
    return {"ok": True}

@app.route("/messages")
def stored_messages_view():
    try:
        after = float(request.args['after'])
    except:
        abort(400)
    filtered_messages = filter_stored_messages(stored_messages, "time", after)
    return {'messages': filtered_messages}

app.run()