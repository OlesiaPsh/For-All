import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multy(self):
        assert self.calc.multiply(self, 3, 5) == 15

    def test_division(self):
        assert self.calc.division(self, 30, 5) == 6

    def test_subtraction(self):
        assert self.calc.subtraction(self, 13, 5) == 8

    def test_adding(self):
        assert self.calc.adding(self, 23, 5) == 28