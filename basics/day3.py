# - **Day 3:** Make a calculator that performs +, -, *, /, //, %, ** on two user inputs.

def calc(var1: int, var2: int, operand: str) -> int:
    if operand == '+':
        return var1 + var2
    elif operand == '-':
       return var1 - var2
    elif operand == '*':
        return var1*var2
    elif operand == '/':
        return var1/var2
    elif operand == '//':
        return var1/var2
    elif operand == '%':
        return var1%var2
    elif operand == '**':
        return var1**var2
    else:
        print("Operand not found!")
        return None 
    
if __name__ == '__main__':
    print("We are going to calculate 2 values!")
    var1 = int(input("Please enter the first integer: "))
    var2 = int(input("Please enter the second integer: "))
    operand = input("Please choose an operand (e.g., +, -, *, /, //, %, **): ")

    print(f"The result is: {calc(var1, var2, operand)}")