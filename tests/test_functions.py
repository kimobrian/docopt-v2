"""Function tests"""
from unittest import TestCase
from functions import Operations

class TestOperations(TestCase):

    def setUp(self):
        """
        seTup operations
        create ops object to be used by all tests
        """
        self.ops = Operations()

    def tearDown(self):
        """tearDown operations"""
        pass

    def test_add_valid_values(self):
        """Test that sum functions returns correct result"""
        summation = self.ops.add(12, 13)
        self.assertEqual(summation, 25)

    def test_add_invalid_values(self):
        """Test that non-digit errors are handled correctly"""
        summation = self.ops.add("brian", 13)
        self.assertEqual(summation, "Invalid Entry")

    def test_multiple_with_no_values(self):
        """Test addition of multiple values without any values"""
        summation = self.ops.add_multiple()
        self.assertEqual(summation, "No numbers provided")

    def test_add_multiple(self):
        """Test addition of multiple values"""
        summation = self.ops.add_multiple(5, 10, 6, 10)
        self.assertEqual(summation, 31)

    def test_add_multiple_with_invalid(self):
        """Test addition of multiple values with invalid values"""
        summation = self.ops.add_multiple(5, "ten", 6, "two")
        self.assertEqual(summation, "Invalid Values")

    def test_multiple_operations_sum(self):
        """Test summation using multiple operations function"""
        summation = self.ops.multiple_operations(12, 40, "+")
        self.assertEqual(summation, 52)

    def test_multiple_operations_subtract(self):
        """Test subtraction using multiple operations function"""
        summation = self.ops.multiple_operations(20, 5, "-")
        self.assertEqual(summation, 15)

    def test_multiple_operations_multiplication(self):
        """Test multiplication using multiple operations function"""
        summation = self.ops.multiple_operations(20, 5, "*")
        self.assertEqual(summation, 100)

    def test_multiple_operations_invalid_sign(self):
        """Test invalid operation using multiple operations function"""
        summation = self.ops.multiple_operations(20, 5, "u")
        self.assertEqual(summation, "Unsupported Operation")

    def test_multiple_operations_invalid_values(self):
        """Test invalid values using multiple operations function"""
        summation = self.ops.multiple_operations(20, "string", "+")
        self.assertEqual(summation, "Invalid Values")

    def test_default_values(self):
        """Test using default arguments"""
        full_name = self.ops.func_default_values()
        self.assertEqual(full_name, "John Doe")
        full_name2 = self.ops.func_default_values("Jack", "Bauer")
        self.assertEqual(full_name2, "Jack Bauer")

    def test_func_optional_values(self):
        """Test using optional arguments"""
        full_name = self.ops.func_optional_values("", "")
        self.assertEqual(full_name, "Jane Doe")
        full_name = self.ops.func_optional_values("Brian", "")
        self.assertEqual(full_name, "Brian")
        full_name = self.ops.func_optional_values("", "Kim")
        self.assertEqual(full_name, "Kim")
