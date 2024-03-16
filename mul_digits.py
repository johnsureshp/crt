# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:13:16 2024

@author: P.JOHN
"""

num = int(input("enter the number"))
temp=0
mul =1
while num >0:
    temp = num%10
    mul = mul*temp
    num = num//10
print(mul)
    