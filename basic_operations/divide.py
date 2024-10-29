class Divide:
    def __init__(self, title="Division"):
        self.title = title
        
    def divide(self, num1, num2):
        result = num1 / num2
        return f"{self.title}: {result:.2f}"
    
    def calculate_division(self):
        numerators = input("Inform the division values (Separate by ','): ")
        numerators = [int(num) for num in numerators.split(",")]
        result = self.divide(*numerators)
        print(result)