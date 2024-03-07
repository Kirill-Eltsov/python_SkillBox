from flask import Flask

app = Flask(__name__)

expenses = {}

@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    expenses[date] = expenses.get(date, 0) + number
    return 'Трата успешно добавлена'

@app.route('/calculate/<int:year>')
def calculate_year(year):
    total_expenses = sum(expense for date, expense in expenses.items() if date.startswith(str(year)))
    return f'Суммарные траты за {year} год: {total_expenses} руб.'

@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    total_expenses = sum(expense for date, expense in expenses.items() if date.startswith(f'{year}{month:02d}'))
    return f'Суммарные траты за {month}.{year}: {total_expenses} руб.'

if __name__ == '__main__':
    app.run()
