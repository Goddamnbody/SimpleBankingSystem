import unittest
from BankingSystem import BankSystem


class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.bank = BankSystem()
        self.bank.create_account('Alice', 1000)
        self.bank.create_account('Bob', 500)

    def test_deposit(self):
        alice = self.bank.get_account('Alice')
        alice.deposit(200)
        self.assertEqual(alice.balance, 1200)

    def test_withdraw(self):
        alice = self.bank.get_account('Alice')
        alice.withdraw(100)
        self.assertEqual(alice.balance, 900)
    
    def test_transfer(self):
        alice = self.bank.get_account('Alice')
        bob = self.bank.get_account('Bob')
        alice.transfer(150, bob)
        self.assertEqual(alice.balance, 750)
        self.assertEqual(bob.balance, 650)

    def test_overdraft(self):
        alice = self.bank.get_account('Alice')
        alice.withdraw(2000)  # Should not allow
        self.assertEqual(alice.balance, 750)  # Balance should remain unchanged
    
    def test_save_load(self):
        self.bank.save_to_csv('test_bank_state.csv')
        new_bank = BankSystem()
        new_bank.load_from_csv('test_bank_state.csv')
        
        alice = new_bank.get_account('Alice')
        bob = new_bank.get_account('Bob')
        
        self.assertEqual(alice.balance, 750)
        self.assertEqual(bob.balance, 650)

if __name__ == '__main__':
    unittest.main()
