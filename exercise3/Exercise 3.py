# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"

# TODO: Call the 'greet' function
# Define a function called 'greet'
def greet():
    print("Hello, World!")

# Call the greet function
greet()

#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting

# TODO: Call the 'personalized_greeting' function with your name
# Define a function that takes a name as a parameter
def personalized_greeting(name):
    print("Hello,", name, "! Welcome!")

# Call the function with your name
personalized_greeting("Shuaib")

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square

# TODO: Call the 'square' function with the number 5 and print the result
# Define a function that returns the square of a number
def square(number):
    return number * number

# Call the function with 5 and print the result
print("Square of 5:", square(5))

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle

# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result

# Define a function that calculates rectangle area
def rectangle_area(length, width):
    return length * width

# Call the function with length 4 and width 5
print("Area of rectangle:", rectangle_area(4, 5))

#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number

# TODO: Define a function called 'double' that takes a number as a parameter and returns its double

# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result

# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
# Define a function that applies another function to a number
def apply_operation(function, number):
    return function(number)

# Define a function that doubles a number
def double(number):
    return number * 2

# Apply double to 7
print("Double of 7:", apply_operation(double, 7))

# Apply square to 3 (function from Question 3)
print("Square of 3:", apply_operation(square, 3))

