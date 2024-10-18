def calculator():
    print("SIMPLE CALCULATOR WITH BASIC ARITHMETIC OPERATIONS")
    print("1.Addition + ")
    print("2.Subtraction -")
    print("3.Multiplication *")
    print("4.Division / ")
    ch=int(input("Enter your choice(1-4):"))
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    if ch==1:
        sum=num1+num2
        print("Sum of two numbers is:",sum)
    elif ch==2:
        sub=num1-num2
        print("Subtraction of two numbers is:",sub)
    elif ch==3:
        mul=num1*num2
        print("Multiplication of two numbers is:",mul)
    elif ch==4:
        div=num1/num2
        print("Division  of two numbers is:",div)
    else:
        print("Invalid choice")
calculator()
