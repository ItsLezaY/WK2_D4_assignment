import math

def calculate_square_footage(length, width):
    return length * width

def calculate_circumference(radius):
    return 2 * math.pi * radius

def calculator_module():
    print("\tHello, please select your choice:\n")
    print("\n1 - Calculate square footage of a house.\n")
    print("\n2 - Calculate circumference of a circle.\n")

    choice = int(input("Enter your choice: \n"))

    if choice == 1:
        length = float(input("\nEnter length of house: "))
        width = float(input("\nEnter width of house: "))
        area = calculate_square_footage(length, width)
        print(f"\nThe square footage of the house is: {area:.2f} square units") # .2f for decimal formatting

    elif choice == 2:
        radius = float(input("\nEnter radius of circle: "))
        circumference = calculate_circumference(radius)
        print(f"\nThe circumference of the circle is: {circumference:.2f}")

    else:
        print("\nPlease select choice 1 or 2.")

calculator_module()