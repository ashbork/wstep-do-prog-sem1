from typing import Type
import random
import unittest


class Employee():
    def __init__(self, first_name: str,
                 last_name: str, annual_salary: int) -> None:
        if not isinstance(first_name, str) or not isinstance(first_name, str):
            raise TypeError("name should be of type str")
        if not isinstance(annual_salary, int):
            raise TypeError("salary should be of type int")
        self.first_name = first_name
        self.last_name = last_name
        self.salary = annual_salary

    def __repr__(self) -> str:
        return f"Employee({self.first_name} {self.last_name})"

    def __str__(self) -> str:
        return f"Employee: {self.first_name} {self.last_name} with an annual salary of {self.salary}."

    def give_raise(self, raise_value=2000) -> None:
        if not isinstance(raise_value, int):
            raise TypeError("raise should be of type int")
        if raise_value <= 0:
            raise ValueError("raise value should be positive")
        self.salary += raise_value


class EmployeeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee("Jan", "Kowalski", 120000)

    def test_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 122000)

    def test_random_raise(self):
        value = random.randint(1, 100000)
        self.employee.give_raise(value)
        self.assertEqual(self.employee.salary, 120000 + value)

    def test_bad_raise_value(self):
        with self.assertRaises(ValueError):
            self.employee.give_raise(-100)

    def test_bad_raise_type(self):
        with self.assertRaises(TypeError):
            self.employee.give_raise(0.5)


if __name__ == '__main__':
    unittest.main()
