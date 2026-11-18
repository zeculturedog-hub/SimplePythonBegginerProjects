print("Enter two numbers")

num1 = float(input("first number: "))
num2 = float(input("second number: "))

print("choose your operator: ")

op = input("Operator: ")

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op =="*":
    print(num1*num2)
elif op =="/":
    print(num1/num2)
else:
    print("invalid operator")
