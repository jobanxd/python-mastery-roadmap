# **Day 2:** Create a function that takes user input and tells the data type of each input (use `type()` and casting).

# Initially inputs are in string.
user_input = input("Hello, give any input: ")
print("Initially the input from user is always a string type.")

# Convert to int
input_int = int(user_input)
print(f"The variable 'input_int': {input_int} is {type(input_int)}")

# Convert to float
input_float = float(user_input)
print(f"The variable 'input_float': {input_float:.2f} is {type(input_int)}")

# Convert again to string
input_str = str(input_float)
print(f"The variable 'input_str': {input_str} is {type(input_str)}")


# Take away - It is always better to convert it to float first before we convert it to int, this is  to prevent error when the given input contains decimal.
