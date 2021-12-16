from tkinter import Tk, Label, Button, Entry

class calculator():

    def addition():
        a=int(input("Enter number:"))
        b=int(input("Enter the 2nd number:"))
        if a>=0:
            print(a," + ",b," = ",a+b)
        else:
            print("Operation not valid, Try again!!") 

    def subtraction():
        a1=int(input("Enter number:"))
        b1=int(input("Enter the 2nd number:"))
        if a1>=0:
            print(a1," - ",b1," = ",a1-b1)
        else:
            print("Operation not valid, Try again!!")         

    def multiplication():
        a2=int(input("Enter number:"))
        b2=int(input("Enter the 2nd number:"))
        if a2>=0:
            print(a2," * ",b2," = ",a2*b2)
        else:
            print("Operation not valid, Try again!!")         

    def division():
        a3=int(input("Enter number:"))
        b3=int(input("Enter the 2nd number:"))
        if a3>=0:
            print(a3," / ",b3," = ",a3/b3)
        else:
            print("Operation not valid, Try again!!")         


print("My Calculator")
print("Choose any number to select!!")
print("For Addition:1")
print("For Subtraction:2")
print("For multiplication:3")
print("For Division:4")

num=int(input("Enter any number to select mathmatical operation:"))
if num==1:
    calculator.addition()  
elif num==2:
    calculator.subtraction()

elif num==3:
    calculator.multiplication()

elif num==4:
    calculator.division()    

else:    
    print("Please Enter valid number!")          

