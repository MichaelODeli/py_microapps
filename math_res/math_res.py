import math
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