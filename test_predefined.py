import unittest
import api
import math

class TestCase:
    """ TestCase class holds information about individual test cases """

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    """ Assign LHS/RHS attributes"""
    def assign(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    """ Calculate and return results as tuple, since a result '0' can be perceived as '0' or '0.0' 
        Both or which are correct """
    def calc_add(self):
        result = self.lhs + self.rhs
        return result, result + 0.0

    def calc_subtract(self):
        result = self.lhs - self.rhs
        return result, result + 0.0

    def calc_divide(self):
        if self.lhs == 0 or self.rhs == 0:
            return 0, float('nan')
        result = self.lhs / self.rhs
        return result, result + 0.0

    def calc_multiply(self):
        result = self.lhs * self.rhs
        return result, result + 0.0


class TestData:
    """ TestData class generates the test data, and compares it """

    """ List of test values of each integer type"""
    positive_even_integers = [0]
    positive_odd_integers = []
    negative_even_integers = [0]
    negative_odd_integers = []

    """ Note:
        Decimals cannot be classed as even or odd, 
        thus single lists are created for both positive & negative decimals """

    """ List of test values for each decimal type """
    positive_decimals = [0]
    negative_decimals = [0]

    """ Test cases, mixed contains test cases which include both integers and decimals """
    test_cases_integers = []
    test_cases_decimals = []
    test_cases_mixed = []

    """ Generate lists of test values for integers (positive/negative, even/odd), and decimals (positive/negative) """
    def __gen_test_values(self, _range):
        for i in range(-_range, _range + 1):
            if i < 0:
                if i % 2:
                    self.negative_odd_integers.append(i)
                else:
                    self.negative_even_integers.append(i)

                self.negative_decimals.append(i - 0.5)
            elif i > 0:
                if i % 2:
                    self.positive_odd_integers.append(i)
                else:
                    self.positive_even_integers.append(i)

                self.positive_decimals.append(i + 0.5)

            else:
                self.positive_even_integers.append(0)
                self.positive_odd_integers.append(0)
                self.negative_even_integers.append(0)
                self.negative_odd_integers.append(0)
                self.positive_decimals.append(0)
                self.negative_decimals.append(0)

    """ Generate test cases from the test values created"""
    def __gen_test_cases(self, _range):

        """ INTEGERS """

        """ Generate test cases for: LHS = Positive Integer, RHS = Positive Integer """
        for i in range(1, _range):
            self.test_cases_integers.append(TestCase(self.positive_even_integers[i], self.positive_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.positive_even_integers[i], self.positive_odd_integers[i]))
            self.test_cases_integers.append(TestCase(self.positive_odd_integers[i], self.positive_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.positive_odd_integers[i], self.positive_odd_integers[i]))

        """ Generate test cases for: LHS = Negative Integer, RHS = Negative Integer """
        for i in range(1, _range):
            self.test_cases_integers.append(TestCase(self.negative_even_integers[i], self.negative_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.negative_even_integers[i], self.negative_odd_integers[i]))
            self.test_cases_integers.append(TestCase(self.negative_odd_integers[i], self.negative_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.negative_odd_integers[i], self.negative_odd_integers[i]))

        """ Generate test cases for: LHS = Positive Integer, RHS = Negative Integer """
        for i in range(1, _range):
            self.test_cases_integers.append(TestCase(self.positive_even_integers[i], self.negative_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.positive_even_integers[i], self.negative_odd_integers[i]))
            self.test_cases_integers.append(TestCase(self.positive_odd_integers[i], self.negative_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.positive_odd_integers[i], self.negative_odd_integers[i]))

        """ Generate test cases for: LHS = Negative Integer, RHS = Positive Integer """
        for i in range(1, _range):
            self.test_cases_integers.append(TestCase(self.negative_even_integers[i], self.positive_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.negative_even_integers[i], self.positive_odd_integers[i]))
            self.test_cases_integers.append(TestCase(self.negative_odd_integers[i], self.positive_even_integers[i]))
            self.test_cases_integers.append(TestCase(self.negative_odd_integers[i], self.positive_odd_integers[i]))

        """ DECIMALS """

        """ Generate test cases for: LHS = Positive Decimal, RHS = Positive Decimal """
        for i in range(1, _range):
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.positive_decimals[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Positive Decimal, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Positive Decimal """
        for i in range(1, _range):
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.positive_decimals[i]))

        """ MIXED """

        """ Generate test cases for: LHS = Positive Integer, RHS = Positive Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_even_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_odd_integers[i], self.positive_decimals[i]))

        """ Generate test cases for: LHS = Negative Integer, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_even_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_odd_integers[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Positive Decimal, RHS = Positive Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.positive_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.positive_odd_integers[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Negative Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.negative_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.negative_odd_integers[i]))

        """ Generate test cases for: LHS = Positive Integer, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_even_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_odd_integers[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Positive Decimal, RHS = Negative Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.negative_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.negative_odd_integers[i]))

        """ Generate test cases for: LHS = Negative Integer, RHS = Positive Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_even_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_odd_integers[i], self.positive_decimals[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Positive Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.positive_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.positive_odd_integers[i]))

        self.test_cases_decimals = list(dict.fromkeys(self.test_cases_decimals))

    def __init__(self,):
        """ Generate test values with _range of values,
            eg, _range = 100, then range of data created is from -50 to 50 """
        self.range = 1 << 3
        self.__gen_test_values(self.range)

        """ Note:   
            Decimals are not classed as either even or odd. There are as many as decimals as there are 
            even & odd integers combined, thus not all decimals are used in the test cases """

        """ Number of test cases = (_range / 2) + 1 """
        self.__gen_test_cases(int((self.range/2)+1))


class TestPredefined(unittest.TestCase):

    """ Range of test cases,
        if range_min = 0, range_max = 10 then this will only test cases from 0-10, providing there are 10 cases """

    range_min = 0
    range_max = 20

    @classmethod
    def setUpClass(cls):
        print("Creating test data..")
        cls.test_data = TestData()
        print("Test data created")

    def test_integer_addition(self):
        print("\nPerforming integer addition tests..")
        for test_case in self.test_data.test_cases_integers[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "+" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_add()
            print('Test: ["' + query + '" == ' + str(test_case.calc_add()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_integer_subtraction(self):
        print("\nPerforming integer subtraction tests..")
        for test_case in self.test_data.test_cases_integers[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "-" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_subtract()
            print('Test: ["' + query + '" == ' + str(test_case.calc_subtract()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_integer_multiplication(self):
        print("\nPerforming integer multiplication tests..")
        for test_case in self.test_data.test_cases_integers[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "*" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_multiply()
            print('Test: ["' + query + '" == ' + str(test_case.calc_multiply()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_integer_division(self):
        print("\nPerforming integer division tests..")
        for test_case in self.test_data.test_cases_integers[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "/" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_divide()
            if not passed:
                if math.isnan(result):
                    """ Assert false = True """
                    print('Test: ["' + query + '" == ' + str(test_case.calc_divide()[1]) + "] " + "True")
                    self.assertFalse(passed)
            else:
                print('Test: ["' + query + '" == ' + str(test_case.calc_divide()[1]) + "] " + str(passed))
                self.assertTrue(passed)

    def test_decimal_addition(self):
        print("\nPerforming decimal addition tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "+" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_add()
            print('Test: ["' + query + '" == ' + str(test_case.calc_add()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_decimal_subtraction(self):
        print("\nPerforming decimal subtraction tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "-" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_subtract()
            print('Test: ["' + query + '" == ' + str(test_case.calc_subtract()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_decimal_multiplication(self):
        print("\nPerforming decimal multiplication tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "*" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_multiply()
            print('Test: ["' + query + '" == ' + str(test_case.calc_multiply()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_decimal_division(self):
        print("\nPerforming decimal division tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "/" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_divide()
            if not passed:
                if math.isnan(result):
                    """ Assert false = True """
                    print('Test: ["' + query + '" == ' + str(test_case.calc_divide()[1]) + "] " + "True")
                    self.assertFalse(passed)
            else:
                print('Test: ["' + query + '" == ' + str(test_case.calc_divide()[1]) + "] " + "True")
                self.assertTrue(passed)

    def test_mixed_addition(self):
        print("\nPerforming mixed addition tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "+" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_add()
            print('Test: ["' + query + '" == ' + str(test_case.calc_add()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_mixed_subtraction(self):
        print("\nPerforming mixed subtraction tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "-" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_subtract()
            print('Test: ["' + query + '" == ' + str(test_case.calc_subtract()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_mixed_multiplication(self):
        print("\nPerforming mixed multiplication tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "*" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_multiply()
            print('Test: ["' + query + '" == ' + str(test_case.calc_multiply()[1]) + "] " + str(passed))
            self.assertTrue(passed)

    def test_mixed_division(self):
        print("\nPerforming mixed division tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "/" + str(test_case.rhs)
            result = api.api(query)
            passed = result in test_case.calc_divide()
            if not passed:
                if math.isnan(result):
                    """ Assert false = True """
                    print('Test: ["' + query + '" == ' + str(test_case.calc_divide()[1]) + "] " + "True")
                    self.assertFalse(passed)
            else:
                print('Test: ["' + query + '" == ' + str(test_case.calc_divide()[1]) + "] " + str(passed))
                self.assertTrue(passed)


def test_predefined():
    """ Executes the tests from another script """

    print("\nPredefined Tests Executing:\n")

    """ Test case range from test case 0 to test case 20 """

    TestPredefined.range_min = 0
    TestPredefined.range_max = 20

    test_loader = unittest.TestLoader()
    test_result = unittest.TestResult()

    test_suite = test_loader.loadTestsFromTestCase(TestPredefined)
    test_suite.run(result=test_result)

    if test_result.wasSuccessful():
        print("\nPredefined Tests Result: ALL PASSED\n")
        return True
    else:
        print("\nPredefined Tests Result: ALL TESTS DID NOT PASS\n")
        return False


if __name__ == "__main__":
    """ By using maximum test case range, the test will run for days,  
        thus test case range from test case 0 to test case 20 """
    TestPredefined.range_min = 0
    TestPredefined.range_max = 20

    unittest.main()
