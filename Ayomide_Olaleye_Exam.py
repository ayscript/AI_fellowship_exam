# Question 1
def addition(a, b):
    return a + b

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

while True:
    user_input = input("\nChoose operation (+, -, *, /) or 'exit' to quit \n\n")
    
    try:
        if user_input == "exit":
            print('Exiting calculator... Goodbye!')
            break
        elif user_input == '/':
            num1 = int(input("Enter the first number (Divisor): "))
            num2 = int(input("Enter the second number (dividend): "))
            try:
                print(f"\nResult: {division(num1,num2)}\n")
            except ZeroDivisionError:
                print("An error occured: You cannot divide a number by 0")
            except Exception as error:
                print(f"An error occured: {error}")
                
        elif user_input == '*':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            try:
                print(f"\nResult: {multiplication(num1, num2)}")
            except Exception as error:
                print(f"An error occured: {error}")
        
        elif user_input == '+':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            try:
                print(f"\nResult: {addition(num1, num2)}\n")
            except Exception as error:
                print(f"An error occured: {error}")
                
        elif user_input == '-':
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            try:
                print(f"\nResult: {subtraction(num1, num2)}\n")
            except Exception as error:
                print(f"An error occured: {error}")
        else:
            raise Exception(f"'{user_input}' is an invalid option")
    except Exception as error:
        print(f"An error occured: {error}")
        
        
        
        
        
        
        
# QUESTION 2 
while True:
    try:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        if user_input == "exit":
            print("Goodbye!")
            break        # break out of loop
        
        num = int(user_input)   # convert to integer
        
        if num % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
    except Exception as e:
        print(f"An error occured: {e}")







# Question 3
while True:
    age = input("Enter your age (or type exit to quit): ")

    
    try:
        if age == "exit":
            print("Goodbye!")
            break
        elif int(age) >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input. Please enter a number")