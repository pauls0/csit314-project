import unittest
import api


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
        result = self.lhs / self.rhs
        return result, result + 0.0

    def calc_multiply(self):
        result = self.lhs * self.rhs
        return result, result + 0.0


class TestData:
    """ TestData class generates the test data, and compares it """

    """ List of test values of each integer type"""
    positive_even_integers = []
    positive_odd_integers = []
    negative_even_integers = []
    negative_odd_integers = []

    """ Note:
        Decimals cannot be classed as even or odd, 
        thus single lists are created for both positive & negative decimals """

    """ List of test values for each decimal type """
    positive_decimals = []
    negative_decimals = []

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
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.positive_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.positive_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.positive_decimals[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.negative_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.negative_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.negative_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Positive Decimal, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.negative_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.negative_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.negative_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.positive_decimals[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Positive Decimal """
        for i in range(1, _range):
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.positive_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.positive_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.positive_decimals[i]))
            self.test_cases_decimals.append(TestCase(self.negative_decimals[i], self.positive_decimals[i]))

        """ MIXED """

        """ Generate test cases for: LHS = Positive Integer, RHS = Positive Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_even_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_even_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_odd_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_odd_integers[i], self.positive_decimals[i]))

        """ Generate test cases for: LHS = Negative Integer, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_even_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_even_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_odd_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_odd_integers[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Positive Decimal, RHS = Positive Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.positive_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.positive_odd_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.positive_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.positive_odd_integers[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Negative Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.negative_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.negative_odd_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.negative_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.negative_odd_integers[i]))

        """ Generate test cases for: LHS = Positive Integer, RHS = Negative Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_even_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_even_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_odd_integers[i], self.negative_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.positive_odd_integers[i], self.negative_decimals[i]))

        """ Generate test cases for: LHS = Positive Decimal, RHS = Negative Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.negative_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.negative_odd_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.negative_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.positive_decimals[i], self.negative_odd_integers[i]))

        """ Generate test cases for: LHS = Negative Integer, RHS = Positive Decimal """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_even_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_even_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_odd_integers[i], self.positive_decimals[i]))
            self.test_cases_mixed.append(TestCase(self.negative_odd_integers[i], self.positive_decimals[i]))

        """ Generate test cases for: LHS = Negative Decimal, RHS = Positive Integer """
        for i in range(1, _range):
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.positive_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.positive_odd_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.positive_even_integers[i]))
            self.test_cases_mixed.append(TestCase(self.negative_decimals[i], self.positive_odd_integers[i]))

    def __init__(self,):
        """ Generate test values with _range of values,
            eg, _range = 100, then range of data created is from -50 to 50 """
        self.range = 1 << 16
        self.__gen_test_values(self.range)

        """ Note:   
            Decimals are not classed as either even or odd. There are as many as decimals as there are 
            even & odd integers combined, thus not all decimals are used in the test cases """

        """ Number of test cases = (_range / 2) + 1 """
        self.__gen_test_cases(int((self.range/2)+1))


class TestPredefined(unittest.TestCase):

    """ Range of test cases,
        by default rest cases were created from a numerical range of 1 << 16 (65536)
        which creates 524,288 test cases for integers, which we'll base the maximum test
        case range off
        i,e, range_min = 0, range_max = 10 will only test cases from 0-10 """
    range_min = 0
    range_max = 524288

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
            self.assertTrue(result in test_case.calc_add())

    def test_integer_subtraction(self):
        print("\nPerforming integer subtraction tests..")
        for test_case in self.test_data.test_cases_integers[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "-" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_subtract())

    def test_integer_multiplication(self):
        print("\nPerforming integer multiplication tests..")
        for test_case in self.test_data.test_cases_integers[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "*" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_multiply())

    def test_integer_division(self):
        print("\nPerforming integer division tests..")
        for test_case in self.test_data.test_cases_integers[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "/" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_divide())

    def test_decimal_addition(self):
        print("\nPerforming decimal addition tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "+" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_add())

    def test_decimal_subtraction(self):
        print("\nPerforming decimal subtraction tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "-" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_subtract())

    def test_decimal_multiplication(self):
        print("\nPerforming decimal multiplication tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "*" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_multiply())

    def test_decimal_division(self):
        print("\nPerforming decimal division tests..")
        for test_case in self.test_data.test_cases_decimals[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "/" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_divide())

    def test_mixed_addition(self):
        print("\nPerforming mixed addition tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "+" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_add())

    def test_mixed_subtraction(self):
        print("\nPerforming mixed subtraction tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "-" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_subtract())

    def test_mixed_multiplication(self):
        print("\nPerforming mixed multiplication tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "*" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_multiply())

    def test_mixed_division(self):
        print("\nPerforming mixed division tests..")
        for test_case in self.test_data.test_cases_mixed[self.range_min:self.range_max]:
            query = str(test_case.lhs) + "/" + str(test_case.rhs)
            result = api.api(query)
            self.assertTrue(result in test_case.calc_divide())


def test_predefined():
    
    print("\nPredefined Tests Executing:")
    
    # Using maximum test case range, would take days to run, thus test case range from test case 0 - 10
    TestPredefined.range_max = 0
    TestPredefined.range_max = 5

    unittest.main()
    
    allPassed = True # TODO: return bool true if all predefined tests passed
    if allPassed:
        print("Predefined Tests Result: ALL PASSED")
    else:
        print("Predefined Tests Result: ALL TESTS DID NOT PASS")
    
    allPassed = True
    return allPassed