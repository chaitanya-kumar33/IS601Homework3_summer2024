
class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  # Store the operation function

    def get_result(self):
        return self.operation(self.a, self.b) # Calls the stored operation with parameters a and b