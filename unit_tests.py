import unittest
from unittest.mock import patch
from data import DataProgram
import operations

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.data_program = DataProgram()
        operations.data_program = self.data_program

    @patch('builtins.input', return_value='500.50')
    @patch('builtins.print')
    def test_credit_valid(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1500.50)
        mock_print.assert_called_with('Amount credited. New balance: 001500.50')

    @patch('builtins.input', return_value='500.50')
    @patch('builtins.print')
    def test_debit_valid(self, mock_print, mock_input):
        operations.run_operation('DEBIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 499.50)
        mock_print.assert_called_with('Amount debited. New balance: 000499.50')

    @patch('builtins.print')
    def test_total(self, mock_print):
        operations.run_operation('TOTAL')
        mock_print.assert_called_with('Current balance: 001000.00')

    @patch('builtins.input', return_value='-50')
    @patch('builtins.print')
    def test_invalid_negative_credit(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        mock_print.assert_called_with('Please enter a positive number greater than zero.')

    @patch('builtins.input', return_value='abc')
    @patch('builtins.print')
    def test_invalid_non_number(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        mock_print.assert_called_with('Please enter a valid number (digits with an optional decimal point).')

    @patch('builtins.input', return_value='0')
    @patch('builtins.print')
    def test_invalid_zero_credit(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        mock_print.assert_called_with('Please enter a positive number greater than zero.')

    @patch('builtins.input', return_value='123.45.67')
    @patch('builtins.print')
    def test_invalid_multiple_decimal(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        mock_print.assert_called_with('Please enter a valid number (digits with an optional decimal point).')

    @patch('builtins.input', return_value='1000000')
    @patch('builtins.print')
    def test_credit_exceed_max_balance(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        mock_print.assert_called_with('Operation cancelled: balance cannot exceed 999 999.99')

    @patch('builtins.input', return_value='999000')
    @patch('builtins.print')
    def test_credit_to_exact_max_balance(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1000.00)
        mock_print.assert_called_with('Operation cancelled: balance cannot exceed 999 999.99')

    @patch('builtins.input', return_value='10000')
    @patch('builtins.print')
    def test_debit_insufficient_funds(self, mock_print, mock_input):
        operations.run_operation('DEBIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1000.00)
        mock_print.assert_called_with('Insufficient funds for this debit.')

    @patch('builtins.input', return_value='500')
    @patch('builtins.print')
    def test_credit_strip_spaces(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1500.00)
        mock_print.assert_called_with('Amount credited. New balance: 001500.00')

    @patch('builtins.input', return_value=' 500 ')
    @patch('builtins.print')
    def test_debit_strip_spaces(self, mock_print, mock_input):
        operations.run_operation('DEBIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 500.00)
        mock_print.assert_called_with('Amount debited. New balance: 000500.00')

    @patch('builtins.input', return_value='9999999')
    @patch('builtins.print')
    def test_credit_exceed_digits(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        mock_print.assert_called_with("Operation cancelled: balance cannot exceed 999 999.99")
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1000.00)

    @patch('builtins.input', return_value='-300')
    @patch('builtins.print')
    def test_invalid_negative_debit(self, mock_print, mock_input):
        operations.run_operation('DEBIT')
        mock_print.assert_called_with("Please enter a positive number greater than zero.")
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1000.00)

    @patch('builtins.input', return_value='0')
    @patch('builtins.print')
    def test_invalid_zero_debit(self, mock_print, mock_input):
        operations.run_operation('DEBIT')
        mock_print.assert_called_with("Please enter a positive number greater than zero.")
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1000.00)

    @patch('builtins.input', return_value='500000')
    @patch('builtins.print')
    def test_large_credit_within_limits(self, mock_print, mock_input):
        self.data_program.operate('WRITE', 100000.00)
        operations.run_operation('CREDIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 600000.00)
        mock_print.assert_called_with("Amount credited. New balance: 600000.00")

    @patch('builtins.input', return_value='999999.99')
    @patch('builtins.print')
    def test_large_debit_within_limits(self, mock_print, mock_input):
        self.data_program.operate('WRITE', 999999.99)
        operations.run_operation('DEBIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 0.00)
        mock_print.assert_called_with("Amount debited. New balance: 000000.00")

    @patch('builtins.input', return_value='1,23')
    @patch('builtins.print')
    def test_credit_with_comma_decimal(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1001.23)
        mock_print.assert_called_with('Amount credited. New balance: 001001.23')

    @patch('builtins.input', return_value='100.123')
    @patch('builtins.print')
    def test_credit_more_than_two_decimals(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1100.12)
        mock_print.assert_called_with('Amount credited. New balance: 001100.12')

    @patch('builtins.input', return_value='1000000')
    @patch('builtins.print')
    def test_credit_exceed_max_input(self, mock_print, mock_input):
        operations.run_operation('CREDIT')
        balance = self.data_program.operate('READ')
        self.assertEqual(balance, 1000.00)
        mock_print.assert_called_with('Operation cancelled: balance cannot exceed 999 999.99')

if __name__ == "__main__":
    unittest.main(verbosity=2)
