
try:
    num1 = float(input("enter first number: "))
    op = input("enter operator: ")
    num2 = float(input("enter second number: "))


    if op == "+":
        print("answer is", num1 + num2,)
    elif op == "-":
        print("answer is",num1 - num2)
    elif op == "*":
        print("answer is",num1 * num2)
    elif op == "/":
        print("answer is",num1 / num2)


    else:
        print("invalid operator")
except:
    print("error")







