# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:00:27 2024

@author: P.JOHN
"""

"""create an atm system:
    display remaing amount in the atm +
    autenticate the user 
    if the user is autentiacate give the following options to choose
    check balance 
    chask withdrawl +
    [show how much balance is remained ]
    chash deposit +
    [show cash]
    mini statement of the last three transctions
    card renewal 
    
    ruppeee--2000
    
    visa---5000
    masterr card--8499
    
    """
class ATM:
    def __init__(self):
        self.balance=0
    def display(self):
        print("total amount ",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("this is your total balance ",self.balance)
    def withdrawl(self,amount):
        if self.balance >= amount:
            
            self.balance=self.balance-amount
        
            print("withdrawl amount ",amount)
            self.display()
            
        else:
 
            print("insufficent balance")

o=ATM()
o.deposit(10000)
o.withdrawl(99)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            print("in sufficient amount")