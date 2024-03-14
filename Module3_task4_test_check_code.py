from datetime import *
import unittest

from Module2.Module3_tests.Module3_task4_code import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("John Doe", 1990, "123 Main St")

    def test_get_age(self):
        current_year = datetime.now().year
        expected_age = current_year - 1990
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "John Doe")

    def test_set_name(self):
        self.person.set_name("Jane Smith")
        self.assertEqual(self.person.get_name(), "Jane Smith")

    def test_set_address(self):
        self.person.set_address("456 Elm St")
        self.assertEqual(self.person.get_address(), "456 Elm St")

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), "123 Main St")

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())


if __name__ == '__main__':
    unittest.main()
