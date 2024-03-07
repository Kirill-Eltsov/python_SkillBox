from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/hello-world/<name>")
def hello_world(name):
    weekdays = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    weekday = datetime.today().weekday()
    greeting = f"Привет, {name}. Хорошего {weekdays[weekday]}!"
    return greeting

if __name__ == "__main__":
    app.run()
