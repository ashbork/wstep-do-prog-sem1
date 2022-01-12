import random
import unittest


class Employee():
    def __init__(self, first_name: str,
                 last_name: str, annual_salary: float | int) -> None:

        # type validation
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("name should be of type str")
        if not isinstance(annual_salary, (int, float)):
            raise TypeError("salary should be of numeric type")
        self.first_name = first_name
        self.last_name = last_name
        # storing salary as a float
        self.salary = float(annual_salary)

    def __repr__(self) -> str:
        return f"Employee({self.first_name} {self.last_name})"

    def __str__(self) -> str:
        return f"Employee: {self.first_name} {self.last_name} with an annual salary of {self.salary}."

    def give_raise(self, raise_value=2000) -> None:
        if not isinstance(raise_value, (float, int)):
            raise TypeError("raise should be of numeric type")
        if raise_value <= 0:
            raise ValueError("raise value should be positive")
        self.salary += float(raise_value)


class EmployeeTestCase(unittest.TestCase):

    # setting up a fixture before each test
    def setUp(self) -> None:
        self.employee = Employee("Jan", "Kowalski", 120000.0)

    def test_default_raise(self):
        # testing the default raise value
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 122000.0)

    def test_random_raise(self):
        # checking a random raise value
        value = random.random() * 1000
        self.employee.give_raise(value)
        self.assertEqual(self.employee.salary, 120000.0 + value)

    def test_bad_raise_value(self):
        # checking for negative raise value
        with self.assertRaises(ValueError):
            self.employee.give_raise(-100.0)

    def test_bad_raise_type(self):
        # checking for wrong raise type
        with self.assertRaises(TypeError):
            self.employee.give_raise("10")


if __name__ == '__main__':
    unittest.main()
