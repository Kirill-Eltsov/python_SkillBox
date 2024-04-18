import csv
import sqlite3


def delete_wrong_fees(
    cur: sqlite3.Cursor,
    wrong_fees_file: str
)->None:
    with open(wrong_fees_file) as csv_file:
        cars = csv.reader(csv_file)
        car_numbers = []
        for i in cars:
            if i[0] != 'car_number':
                car_numbers.append(i[0])
        car_numbers_tuple = tuple(car_numbers)
        query = f"DELETE FROM table_fees WHERE truck_number IN {car_numbers_tuple}"
        cur.execute(query)
        print(f"Данные с номерами автомобилей {car_numbers_tuple}-\были удалены")

if __name__ == '__main__':
    with sqlite3.connect("hw.db") as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
        conn.commit()