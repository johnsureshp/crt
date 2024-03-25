# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:59:00 2024

@author: P.JOHN
"""

import pandas as pd
class DF:
    def __init__(self):
        self.data = {'acc_no':[],
                'acc_name':[],
                'balance':[]}
    def entires(self,n):
        for i in range(n):
            acc_no = input(f"enter the account number {i+1}    ---> ")
            acc_name = input(f"enter the account holder name {i+1} ---> ")
            balance =float(input(f"enter balance in account {i+1}---> "))
            
            self.data['acc_no'].append(acc_no)
            
            self.data['acc_name'].append(acc_name)
            
            self.data['balance'].append(balance)
            
        #df = pd.DataFrame(self.data)
    def details(self):
        
        df = pd.DataFrame(self.data)
        print(df)
    
    
d = DF()
n = int(input("how many your entering :"))

d.entires(n)    
print(d.details()) 