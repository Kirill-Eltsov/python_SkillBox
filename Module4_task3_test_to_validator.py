import unittest

from Module4.Module4_task1 import app


class TestRegistrationFormValidation(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_valid_email(self):
        response = self.app.post('/registration', data=dict(
            email='test@example.com',
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        response = self.app.post('/registration', data=dict(
            email='invalid_email',
        ))
        self.assertEqual(response.status_code, 400)

    def test_valid_phone(self):
        response = self.app.post('/registration', data=dict(
            phone='1234567890',
        ))
        self.assertEqual(response.status_code, 200)

    def test_invalid_phone(self):
        response = self.app.post('/registration', data=dict(
            phone='12345',
        ))
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
