import unittest

from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction_csv(self):
        test_sub= CsvReader("Tests/Data/subtraction.csv").data
        for row in test_sub: 
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    # def test_subtraction(self):
    #     test_data = CsvReader("Tests/Data/subtraction.csv").data
    #     for row in test_data:
    #         result = float(row['Result'])
    #         self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
    #         self.assertEqual(self.calculator.result, result)

    def test_addition_csv(self):
        test_add = CsvReader("Tests/Data/addition.csv").data
        for row in test_add:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_square_csv(self):
        test_sq= CsvReader("Tests/Data/square.csv").data
        for row in test_sq:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result']))

    def test_multiplication_csv(self):
        test_mul= CsvReader("Tests/Data/multiplication.csv").data
        for row in test_mul:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_division_csv(self):
        test_div= CsvReader("Tests/Data/division.csv").data
        for row in test_div:
            result = round(self.calculator.divide(int(row['Value 2']), int(row['Value 1'])), 7)
            self.assertEqual(result, round(float(row['Result']),7))

    def test_squareroot_csv(self):
        test_sqroot= CsvReader("Tests/Data/root.csv").data
        for row in test_sqroot:
            result = round(self.calculator.squareroot(int(row['Value 1'])), 8)
            self.assertEqual(result, round(float(row['Result']),8))


    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()