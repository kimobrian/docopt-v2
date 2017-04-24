class Operations:
    def __init__(self):
        """Application Constructor"""
        pass

    def add(self, a, b):
        """Adding two numbers"""
        try:
            return a + b
        except:
            return "Invalid Entry"

    def add_multiple(self, *args):
        """Adding multiple numbers"""
        if not args:
            return "No numbers provided"
        total = 0
        try:
            for value in args:
                total += value
            return total
        except:
            return "Invalid Values"

    def multiple_operations(self, a, b, sign):
        try:
            if sign == "+":
                return a + b
            elif sign == "*":
                return a*b
            elif sign == "-":
                return a-b
            else:
                return "Invalid Operation"
        except:
            return "Invalid Values"

    def func_default_values(self, first_name="John", last_name="Doe"):
        """Function using default values"""
        return first_name + " " + last_name

    def func_optional_values(self, first_name, last_name):
        """Function using optional values"""
        if not first_name and not last_name:
            return "Jane Doe"
        elif not first_name and last_name:
            return last_name
        elif not last_name and first_name:
            return first_name
