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

def test_deposit_negative_amount():
    account1 = Account("Owner1")
    with pytest.raises(ValueError):        
        account1.deposit(-5.5)
    
    

def test_withdraw_more_than_balance():
    account1 = Account("Owner1", 1)
    account1.withdraw(2)
    assert pytest.raises(Exception)

def test_withdraw_negative_amount():
    account1 = Account("Owner1", 1)
    account1.withdraw(-2)
    assert pytest.raises(Exception)