def add_numbers(num1, num2):
    return num1 + num2


def calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print("The sum of", num1, "and", num2, "is:", result)


if __name__ == "__main__":
    calc()
