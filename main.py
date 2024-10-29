from basic_operations import Sum, Divide, Multiply, Subtract
import textwrap


def calculator_interface():
    menu = """\n
    ================ CALCULATOR ================
    [+]\tSum
    [/]\tDivide
    [*]\tMultiply
    [-]\tSubtract
    [q]\tExit
    => """

    return input(textwrap.dedent(menu))


if __name__ == "__main__":

    while True:
        option = calculator_interface()

        if option == "+":
            calc = Sum()
            calc.calculate_sum()

        elif option == "/":
            calc = Divide()
            calc.calculate_division()
            
        elif option == "*":
            calc = Multiply()
            calc.calculate_multiply()
            
        elif option == "-":
            calc = Subtract()
            calc.calculate_subtraction()

        elif option == "q":
            break

        else:
            print("Operation invalid. Please choose the operation again.")
