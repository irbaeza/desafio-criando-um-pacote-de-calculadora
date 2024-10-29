class Multiply:

    def __init__(self, title="Multiplication"):
        self.title = title
        
    def multiply(self, *numbers):
        result = 1
        for num in numbers:
            result*= num
        return f"{self.title}: {result:.2f}" 
      
    def calculate_multiply(self):
        numerators = input("Inform the multiplication values (Separate by ','): ")
        numerators = [int(num) for num in numerators.split(",")]
        result = self.multiply(*numerators)
        print(result)