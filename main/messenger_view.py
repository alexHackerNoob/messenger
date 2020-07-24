from PyQt5 import QtWidgets, QtCore
from clientui import Ui_MainWindow
import requests
from messages import format_message
from time_functions import getCurrentUnformattedTime

class ExampleApp(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, url):
        super().__init__()
        super().setupUi(self)
        #connecting
        self.pushButton.pressed.connect(self.send_message)
        self.after = getCurrentUnformattedTime() - 24 * 60 * 60
        self.url = url
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)

    def update_messages(self):
        try:
            response = requests.get(f'{self.url}messages', params={'after': self.after})
        except:
            return
        messages = response.json()['messages']
        for message in messages:
            self.add_text(format_message(message))
            self.after = message['time']


    def send_message(self):
        name = self.lineEditName.text()
        password = self.lineEditPassword.text()
        text = self.textEdit.toPlainText()

        if not name or not password or not text:
            self.add_text("Заполните данные")
            return
        message = {'name': name, 'text': text, 'password': password}
        try:
            response = requests.post(f'{self.url}send', json=message)
        except:
            self.add_text("Сервер недоступен")
            return

        if (response.status_code == 200):
            pass
            #why not message
        elif response.status_code == 401:
            self.add_text("Неправильные имя и фамилия")
            # TODO
        else:
            self.add_text("Ошибка")

    def add_text(self, text):
        self.textBrowser.append(text)
        self.textBrowser.repaint()

app = QtWidgets.QApplication([])
window = ExampleApp("http://127.0.0.1:5000/")
window.show()
app.exec_()