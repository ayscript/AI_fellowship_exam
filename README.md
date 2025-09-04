This is a solution to the AI fellowship exam

# Question 1
## This is a simple calculator
I used functions for each arithmetic operations: Multiplication, Division, Addition and Subtraction

```addition(a, b)```, ```subtraction(num1, num2)```, ```multiplication(num1, num2)``` and ```division(num1, num2)```

# Question 2
##  This is a code completion challenge
A code is given and it is required to complete the mising parts
```
while ____
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit"__
        print("Goodbye!")
        ______        # break out of loop
    
    num = __________(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is ______")
    ___
        print("The number is ______")
```

# Question 3
## is a code correction exercise
There was a runtime error on the given code and it was required to correct the error.
These are the errors and how I solved it:
- valueError: the value age given through input is compared with 18 (which is an integer) when a string is provided it raises a value error, I solved this by typecasting age into int before comparing it with 18
- semantic error: while typing 'exit' to quit the loop, the loop did not quit, I moved the code that checks if age == "exit" into the try block to correct this

```
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == exit:
        print("Goodbye!")
        break
    
    try:
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")
```