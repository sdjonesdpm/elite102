import sqlite3
import unittest
import core_functions


class TestBankingApp(unittest.TestCase):
    def setUp(self):
        """Runs before every test: Set up a shared in-memory database."""
        # Using a 'file' URI with cache=shared keeps the memory DB alive 
        # as long as at least one connection is open.
        core_functions.DB_NAME = 'file:testdb?mode=memory&cache=shared'
        
        # We must manually open one connection here to keep the DB 'alive' 
        # throughout the test logic.
        self.connection = sqlite3.connect(core_functions.DB_NAME, uri=True)
        
        core_functions.create_table()

    def tearDown(self):
        """Runs after every test: Close the persistent connection."""
        self.connection.close()
    
    def test_create_account(self):
        #Test account creation in database.
        core_functions.create_account("John Doe", 500.0)
        balance = core_functions.check_balance(1)
        self.assertEqual(balance, 500.0)

    def test_deposit(self):
        #Test if deposit increases balance correctly.
        core_functions.create_account("Jane Doe", 450.0)
        core_functions.deposit(1, 50.0)
        self.assertEqual(core_functions.check_balance(1), 500.0)

    def negative_deposit(self):
        #Test that negative deposits result in an error.
        core_functions.create_account("Bob Bullock", 400.0)
        with self.assertRaises(ValueError):
            core_functions.deposit(1, -100.0)

    def test_withdraw_success(self):
        #Test a successful withdrawal.
        core_functions.create_account("Carl Stryker", 300.0)
        success = core_functions.withdraw(1, 100.0)
        self.assertTrue(success)
        self.assertEqual(core_functions.check_balance(1), 200.0)

    def test_withdraw_insufficient_funds(self):
        #Test that you cannot withdraw more than the balance.
        core_functions.create_account("Alice Smith", 200.0)
        success = core_functions.withdraw(1, 250.0)
        self.assertFalse(success)
        self.assertEqual(core_functions.check_balance(1), 200.0)

    def test_withdraw_negative_amount(self):
        #Test that negative withdrawals result in an error.
        core_functions.create_account("Eve Adams", 350.0)
        with self.assertRaises(ValueError):
            core_functions.withdraw(1, -50.0)

    def test_check_balance_nonexistent(self):
        #Test that check balance on a nonexistent account returns None.
        balance = core_functions.check_balance(999)
        self.assertIsNone(balance)

if __name__ == '__main__':
    unittest.main()
    
