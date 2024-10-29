class Sum:
    
    def __init__(self, title="Sum"):
        self.title = title
        
    def add (self, *numbers):
        result = sum(numbers)
        return f"{self.title}: {result:.2f}"

    def calculate_sum(self):
        numerators = input("Inform the sum values (Separate by: ','): ")
        numerators = [int(num) for num in numerators.split(",")]
        result = self.add(*numerators)
        print(result)
    