# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:19:36 2024

@author: P.JOHN
"""

class father:
    def bike(self):
        print("tvs xl")
    def laptop(self):
        print("laptop with 2gb")
class child(father):
    def laptop(self):
        print("as per my requirement ")
        print("laptop with 8gb and 512ssd")
        
o=child()
o.laptop()
    