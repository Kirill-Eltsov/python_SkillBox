from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    number_list = numbers.split('/')
    if all(num.isdigit() for num in number_list):
        number_list = [int(num) for num in number_list]
        max_num = max(number_list)
        return f"Максимальное число: {max_num}"
    else:
        return "Ошибка: переданы некорректные данные"


if __name__ == '__main__':
    app.run()
