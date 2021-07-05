from art import logo

print(logo)

# calculator

# operation functions


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operator_dic = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("What's the first number?: "))

    for operation in operator_dic:
        print(operation)
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operator_dic[operation]
        answer = calculation_function(num1, num2)

        print("{} {} {} = {}".format(num1, operation,
                                     num2, answer))
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
