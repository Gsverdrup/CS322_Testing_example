import pytest
from bank import Account

def test_initial_balance():
    account1 = Account("Owner1")
    assert account1.balance == 0
    account2 = Account("Owner2", 5)
    assert account2.balance == 5

def test_deposit():
    account1 = Account("Owner1")
    account1.deposit(5.5)
    assert account1.balance == 5.5

def test_withdraw():
    account2 = Account("Owner2", 5)
    account2.withdraw(3.2)
    assert account2.balance == 1.8