import unittest

from Module2.Module2_task7 import expenses, app


class TestFinancialApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        expenses.clear()
        expenses['20220101'] = 100
        expenses['20220102'] = 200
        expenses['20220201'] = 300
        expenses['20220301'] = 150

    def setUp(self):
        self.app = app.test_client()

    def test_add_expense(self):
        response = self.app.get("/add/20220301/150")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(expenses['20220301'], 150)

    def test_calculate_year(self):
        response = self.app.get("/calculate/2022")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Суммарные траты за 2022 год: 750 руб.")

    def test_calculate_month(self):
        response = self.app.get("/calculate/2022/01")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Суммарные траты за 1.2022: 300 руб.")

    def test_invalid_date_format(self):
        response = self.app.get("/add/20220301/150")
        self.assertEqual(response.status_code, 200)

    def test_empty_storage(self):
        expenses.clear()
        response = self.app.get("/calculate/2022")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Суммарные траты за 2022 год: 0 руб.")


if __name__ == '__main__':
    unittest.main()
