from account import Account
import requests

class CheckingAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount, date):
        self.balance += amount

