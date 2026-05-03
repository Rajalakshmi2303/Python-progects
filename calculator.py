print("simple calculator")
num1=float(input("enter first number;"))
num2=float(input("enter second number;"))
print("choose operation: +,-,*,/,%")
op=input("enter operation;")
if (op=='+'):
    print("result:"num1+num2)
elif(op=='-'):
    print("result;"num1-num2)
elif(op=='*'):
    print("result;"num1*num2)
elif(op=='/'):
    if(num2!=0):
        print("result;"num1/num2)
    else:
        print("cannot divide by zero")
elif(op=='%'):
     print("result;"num1%num2)
else:
    print("invalid operation")