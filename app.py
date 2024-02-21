import datetime
import random

from flask import Flask

app = Flask(__name__)

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
counter = 0

@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'


@app.route('/cars')
def get_cars():
    cars_string = ', '.join(cars)
    return cars_string


@app.route('/cats')
def get_cat():
    random_cat = random.choice(cats)
    return random_cat


@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return f'Точное время: {current_time}'


@app.route('/get_time/future')
def get_time_after_hour():
    current_time = datetime.datetime.now()
    time_after_hour = current_time + datetime.timedelta(hours=1)
    time_after_hour_str = time_after_hour.strftime('%H:%M:%S')
    return f'Точное время через час будет {time_after_hour_str}'


def get_random_word():
    with open('war_and_peace.txt', 'r') as file:
        text = file.read()
    words = text.split()
    random_word = random.choice(words)
    random_word = random_word.strip('.,?!;:"\'[]{}()-_')
    return random_word


@app.route('/get_random_word')
def show_random_word():
    random_word = get_random_word()
    return f'Случайное слово из книги "Война и мир": {random_word}'


@app.route('/counter')
def get_counter():
    global counter
    counter += 1
    return f'Число открытий страницы: {counter}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)