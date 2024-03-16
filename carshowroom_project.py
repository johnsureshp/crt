# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:14:37 2024

@author: P.JOHN
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:54:09 2024

@author: P.JOHN
"""

class pj_showroom:
    cgst=10/100
    sgst = 15/100
    inc = 10/100  
    total = 0
    
    def __init__(self):
        self.list_of_cars = {"TOYATA":["x1","x2","x3"],"MAHINDRA":["t1","t2","t3"] , "MERCEDES":["m1","m2","m3"]}
        
    
    def cars_available(self):
        print()
        print("----AVAILABLE COMPANY CARS IN THE SHOWROOM---- ")
        print()
        for car in self.list_of_cars:
            print()
            print("-->   ",car)
        print()
    def models_available(self,selectedcar):
        
        print()
        print(f" ********WELL COME TO THE {selectedcar} FAMILY ********")
        print()
        print("----AVAILABLE MODELS IN THAT MODEL----")
        if selectedcar in self.list_of_cars:
            for carmodel in self.list_of_cars[selectedcar]:
                print("---->  ",carmodel)
    def variant(self,selectedcar,model):
        self.p=0
        self.sg=0
        self.cg=0
        self.ins=0
        if selectedcar in self.list_of_cars:
            if model in self.list_of_cars[selectedcar]:
                print()
                if selectedcar == "TOYATA" and model == "x1":
                    print("IT IS A DISEAL CAR")
                    
                    self.p=100000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print("thee total price is ",self.total)
                    
                    
                    
                elif selectedcar == "TOYATA" and model == "x2":
                    
                    print("IT IS A DISEAL CAR")
                    self.p=100000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print("thee total price is ",self.total)
                    
                elif selectedcar == "TOYATA" and model == "x3":
                    print("IT IS A PETROL CAR")
                    self.p=200000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print("thee total price is ",self.total)
                    
                elif selectedcar == "MAHINDRA" and model == "t1":
                    print("IT IS A DISEAL CAR")
                    self.p=300000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print("thee total price is ",self.total)
                    
                elif selectedcar == "MAHINDRA" and model == "t2":
                    print("IT IS A PETROL CAR")
                    self.p=400000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print("thee total price is ",self.total)
                    
                elif selectedcar == "MAHINDRA" and model == "t3":
                    print("IT IS A DISEAL CAR")
                    self.p=500000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                   # print("thee total price is ",self.total)
                    
                elif selectedcar == "MERCEDES" and model == "m3":
                    print("IT IS A PETROL CAR")
                    self.p=600000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print("thee total price is ",self.total)
                    
                elif selectedcar == "MERCEDES" and model == "m3":
                    print("IT IS A DISEAL CAR")
                    self.p=700000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print("thee total price is ",self.total)
                    
                elif selectedcar == "MERCEDES" and model == "m3":
                    print("IT IS A PETROL CAR")
                    self.p=800000
                    self.sg=self.p*self.sgst
                    self.cg=self.p*self.cgst
                    self.ins=self.p*self.ins
                    self.total = self.p+self.sg+self.cg+self.ins
                    #print(f"----THE ON ROAD COST OF CAR  {self.selectedcar} OF {self.model} ",self.total)
                    
    def display(self,selectedcar,model,):
        print("-----------------------------------------")
        print("------------DETAILS----------------")
        print("THE CAR COMPANY YOU ARE SELECTED ",selectedcar)
        print("THE MODEL OF THE CAR IS ",model)
        self.variant(selectedcar, model)
        print("THE SHOWROOM PRICE OF THE CAR IS ",self.p)
        print("THE ON ROAD PRICE OF THE CAR IS ",self.total)
    def user_check(self):
        self.cars_available()
        selectedcar = str(input("SELECT THE CAR COMPANY  --->   ")).upper()
        print()
        print(selectedcar)
        if selectedcar not in self.list_of_cars:
            print("INVALID ENTRIE  ")
            print("PLEASE ENTER AVAILABLE CAR COMPANY AGAIN ")
        else:
            self.models_available(selectedcar)
            
        #self.models_available(selectedcar)
        model = input("----ENTER THE MODEL CAR YOU WANT ----").lower()

        
        if model not in self.list_of_cars[selectedcar]:
            print()
            print("-----------INVALID MODEL--------------")
            print()
            print("---ENTER  ONLY AVAILABLE MODELS IN THE SHOWROOM --- ")
        else:
            #fuel = input("enter the fuel type you want  ").lower()
            
            self.variant(selectedcar,model)
            self.display(selectedcar,model)
            
            
        #self.variant(selectedcar,model)
        #self.display(selectedcar,model)
        
        
        
sir = pj_showroom()

sir.user_check()




























                