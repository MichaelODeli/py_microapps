import math
from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
def dev():
    print("Stub for developing applications")
    input()

def tax_calc():
    print("RUS tax calculator for RUPOST packages. Actual for 2020")
    price=float(input("Enter price (in your currency) of your package - "))
    weight=float(input("Enter weight of your package - "))
    print("Enter your currency rate to EUR.")
    currency=float(input("Example: the rate of 1 EUR to RUB as of 15.10.2020 is 90.71. Therefore, you need to enter '90.71'"))
    percent=15
    max_price=currency*300
    tax=0
    if price>max_price or weight>31:
        if price>max_price and weight<31: tax=(percent*0.01)*(price-max_price)
        if weight>31 and price<max_price: tax=(percent*0.01)*(weight-31)
        if weight>31 and price>max_price:
            tax0=(percent*0.01)*(price-max_price)
            tax1=(percent*0.01)*(weight-31)
            if tax0>tax1: tax=tax0
            if tax1>tax0: tax=tax1
            if tax1==tax0: tax=tax1
        tax=str(tax)
        print("Ваш налог "+tax+ " RUB.")
    else:
        print("Поздравляю. Налога нет.")
    input()
def deliteli():
    number=int(input("Enter number: "))
    deliteli=[]
    delitel=1
    while number!=delitel:
        if number%delitel==0:
            deliteli.append(delitel)
        delitel+=1
    deliteli.append(number)
    print("There are divisors by the number "+str(number))
    print(deliteli)
    for del_cur in deliteli:
        del_cur_1=int(number/del_cur)
        print(str(number)+"/"+str(del_cur)+" = "+str(del_cur_1))
    input()
def sin_cos_tan():
    try:
        sinx=int(input("Num to find SIN -  "))
    except: nothing=0
    try:
        cosy=int(input("Num to find COS - "))
    except: nothing=0
    try:
        tang=int(input("Num to find TAN -  "))
    except: nothing=0
    print("Radians (rad) или degrees (deg)?")
    rad_deg=str(input("Enter the abbreviation shown in parentheses above - "))
    if rad_deg=="rad":
        try:
            print("COS = "+str(math.cos(cosy)))
        except: nothing=0
        try:
            print("SIN = "+str(math.sin(sinx)))
        except: nothing=0
        try:
            print("TG = "+str(math.tan(tang)))
        except: nothing=0
    if rad_deg=="deg":
        try:
            print("COS = "+str(math.degrees(math.cos(cosy))))
        except: nothing=0
        try:
            print("SIN = "+str(math.degrees(math.sin(sinx))))
        except: nothing=0
        try:
            print("TG = "+str(math.degrees(math.tan(tang))))
        except: nothing=0
    input()
def summa():
    a=int(input("A= "))
    b=int(input("B= "))
    c=a+b
    c=str(c)
    print("Sum="+c)
    input()
def umnoz():
    a=int(input("A= "))
    b=int(input("B= "))
    c=a*b
    c=str(c)
    print("Answer="+c)
    input()
def razn():
    a=int(input("A= "))
    b=int(input("B= "))
    c=a-b
    c1=b-a
    c=str(c)
    c1=str(c1)
    print("A-B="+c)
    print("B-A="+c1)
    input()
def delen():
    a=int(input("A= "))
    b=int(input("B= "))
    if a!=0 and b!=0:
        c=round(a/b, 4)
        c1=round(b/a, 4)
        c=str(c)
        c1=str(c1)
        print("A/B="+c)
        print("B/A="+c1)
    if a==0 or b==0:
        print("Answer: 0")
    input()
def percent():
    print("A - S % (as rule, S=100%)")
    print("B - V %")
    print("If you want to find the value of a specific variable, enter -1 ")
    A=float(input("A= "))
    S=float(input("S (%)= "))
    B=float(input("B= "))
    V=float(input("V (%)= "))
    if A==(-1):
        A=(B*S)/V
        print("A= "+str(A))
    if S==(-1):
        S=(A*V)/B
        print("S= "+str(S))
    if B==(-1):
        B=(A*V)/S
        print("B= "+str(B))
    if V==(-1):
        V=(B*S)/A
        print("V= "+str(V))
    input()

def math_menu_easy():
    math_menu = ConsoleMenu("Math apps. Easy operations", "by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
    math_sum = FunctionItem("Sum (+)", summa)
    math_multi = FunctionItem("Multiplication (*)", umnoz)
    math_subtr = FunctionItem("Subtraction (-)", razn)
    math_div = FunctionItem("Division (/)", delen)
    math_perc = FunctionItem("Percent (%)", percent)
    math_sins = FunctionItem("Sin, Cos, Tg", sin_cos_tan)
    math_deliteli= FunctionItem("Divisors", deliteli)
    math_menu.append_item(math_sum)
    math_menu.append_item(math_multi)
    math_menu.append_item(math_subtr)
    math_menu.append_item(math_div)
    math_menu.append_item(math_perc)
    math_menu.append_item(math_sins)
    math_menu.append_item(math_deliteli)
    math_menu.show()

def math_menu_money():
    math_menu = ConsoleMenu("Math apps. Money operations", "by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
    math_tax = FunctionItem("Tax calculator (to RUS, 2020)", tax_calc)
    math_menu.append_item(math_tax)
    math_menu.show()

