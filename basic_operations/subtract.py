class Subtract:
    def __init__(self, title="Subtraction"):
        self.title = title
        
    def subtract(self, *numbers):
        if len(numbers) == 0:
            print("No numbers provided for subtraction.")
            return "No numbers provided for subtraction."
        
        result = numbers[0]
        for num in numbers[1:]:
            result-= num
            
        return f"{self.title}: {result:.2f}" 

    def calculate_subtraction(self):
        numerators = input("Inform the subtraction values (Separate by: ','): ")
        numerators = [int(num) for num in numerators.split(",")]
        result = self.subtract(*numerators)
        print(result)