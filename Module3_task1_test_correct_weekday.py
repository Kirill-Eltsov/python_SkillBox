import datetime
import unittest

from Module2.Module2_task4 import app, weekdays


class TestCorrectWeekday(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_correct_weekday(self):
        response = self.app.get("/hello-world/Kirill")
        weekday = datetime.datetime.today().weekday()
        expected_greeting = f"Привет, Kirill. {weekdays[weekday]}!"
        self.assertEqual(response.data.decode("utf-8"), expected_greeting)


if __name__ == '__main__':
    unittest.main()
