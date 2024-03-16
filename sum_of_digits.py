# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:58:26 2024

@author: P.JOHN
"""

num = int(input("enter the number :"))
temp =0
summ =0
while num>0:
    temp= num%10
    summ = temp +summ
    num = num//10
print(summ)
    