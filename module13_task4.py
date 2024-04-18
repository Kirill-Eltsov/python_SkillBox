import sqlite3

IVAN_SALARY = 100000

def ivan_savin_the_most_effective(
    cursor_ivan: sqlite3.Cursor,
    name_employee: str,
)-> None:
    response = cursor_ivan.execute(f"SELECT salary FROM table_effective_manager WHERE name = '{name_employee}'")
    salary = response.fetchone()[0]
    salary_after = salary + (salary / 10)
    print(f"Зарплата сотрудника {name_employee} после повышения: {salary_after}")

    if salary_after < IVAN_SALARY:
        print("Зарплата сотрудника увеличивается на 10 процентов.")

        cursor_ivan.execute(
            f"UPDATE table_effective_manager SET salary = {int(salary_after)} WHERE name = '{name_employee}'")
    else:
        print(f"Сотрудник {name_employee} уволен!")
        cursor_ivan.execute(f"DELETE FROM table_effective_manager WHERE name = '{name_employee}'")

if __name__ == '__main__':
    name: str = input('Введите имя сотрудника: ')
    with sqlite3.connect('hw.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        ivan_savin_the_most_effective(cursor, name)
        conn.commit()