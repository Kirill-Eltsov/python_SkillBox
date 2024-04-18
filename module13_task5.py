import sqlite3
import random

TEAMS = [
    ('Австралия', 'Войцих', 'средняя'), ('Австрия', 'РБ', 'сильная'),
    ('Азербайджан', 'Хумелс', 'средняя'), ('Аргентина', 'Де портиво Сантьяго', 'сильная'),
    ('Армения', 'Громстаз', 'средняя'), ('Беларусь', 'Шинник', 'сильная'),
    ('Бельгия', 'Бандиты', 'сильная'), ('Болгария', 'Федеро', 'средняя'),
    ('Бразилия', 'Санта фе', 'сильная'), ('Великобритания', 'Редбулл', 'слабая'),
    ('Венгрия', 'Кракен', 'слабая'), ('Венесуэла', 'Трип', 'слабая'),
    ('Греция', 'Пирей', 'сильная'), ('Грузия', 'Олимпиакос', 'слабая'),
    ('Египет', 'Аль хиляль', 'средняя'), ('Израиль', 'Ишхад', 'сильная'),
    ('Германия', 'Байер', 'средняя'), ('Франция', 'Монако', 'слабая'),
    ('Испания', 'Жирона', 'сильная'), ('Италия', 'Интер Милан', 'слабая')]

TEAM_LEVELS = ['слабая', 'средняя', 'сильная']


def generate_test_data() -> None:
    if not cursor.execute("SELECT EXISTS (SELECT * FROM uefa_commands)"):
        print('Выполняем код')
        cursor.executemany(
            f"INSERT INTO uefa_commands (command_country, command_name, command_level) VALUES (?, ?, ?)",
            TEAMS
        )

    else:
        print("Выполняем жеребьёвку")
        cursor.execute("DELETE FROM uefa_draw")
        for number in range(1, number_of_groups + 1):
            groups = []
            for i in range(3):
                response = cursor.execute(
                    f"SELECT command_number FROM uefa_commands WHERE command_level = '{TEAM_LEVELS[1]}'"
                )
                com_num = response.fetchall()
                if com_num:
                    if i == 1:
                        new_tuple = (number,)
                        new_tuple = new_tuple + random.choice(com_num)
                        groups.append(new_tuple)
                    new_tuple = (number,)
                    new_tuple = new_tuple + random.choice(com_num)
                    groups.append(new_tuple)
            cursor.executemany(
                f"INSERT INTO uefa_draw (group_number, command_number) VALUES (?, ?)", groups
            )


if __name__ == '__main__':
    number_of_groups: int = int(input('Введите количество групп (от 4 до 16): '))
    with sqlite3.connect('hw.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        generate_test_data()
        conn.commit()
