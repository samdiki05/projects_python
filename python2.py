
def get_number(number):
    while True:
        operand = input("Number " + str(number) + ": ")
        try:
            return float(operand)            
        except:
            print("Invalid number, try again. ")

operand = get_number(1)
operand2 = get_number(2)
sign = input("Sign:  ")


result = 0
if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "/":
    if operand2 != 0:
        result = operand / operand2
    else:
        print("Division by zero.")
elif sign == "*":
    result = operand * operand2
    print("Invalid number. ")

print(result)




""" operant = input("Number 1: ")
operant2 = input("Number 2: ")
sign = input("Sign: ")

print(operant, sign, operant2)

 try:
    operant = float(operant)
    operant2 = float(operant2)
    valid = True
except:
    print("Invalid operands. ")

if valid:
  
"""
