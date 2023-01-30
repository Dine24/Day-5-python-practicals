g=input("enter the grade=")
if(g=='C'):
     print("INVALID ENTER A OR B")
     g=input("enter the grade=")
s=int(input("enter the salary="))
if(g=='A')&(s>10000):
    print("your salary is=",s)
    print("bonus amt=",s*0.05)
    print("your bonus salary is=",s*0.05+s)
if(g=='A')&(s<10000):
    print("your salary is=",s)
    print("bonus amt=",s*0.07)
    print("your bonus salary is=",s*0.07+s)
elif(s==0):
    print("enter a valid salary")
elif(s<0):
    print("enter a valid salary")
elif(g=='B')&(s>10000):
    print("your salary is=",s)
    print("bonus amt=",s*0.1)
    print("your bonus salary is=",s*0.1+s)
elif(g=='B')&(s<10000):
    print("your salary is=",s)
    print("bonus amt=",s*0.07)
    print("your bonus salary is=",s*0.07+s)
