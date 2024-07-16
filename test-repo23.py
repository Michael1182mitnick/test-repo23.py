# write a program to check if a given numbers is even or odd
# Function to check if a number is even or odd

def check_even_odd(numbers):
    # if the number is divisible by 2, it's even
    if numbers % 2 == 0:
        return "Even number"
    else:
        # if it's not divisible by 2, it's odd
        return "Odd number"

num = int(input("Enter a numbers: "))
result = check_even_odd(num)
print(f"The numeber: {num} is {result}")