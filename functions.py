class Operations:
    def __init__(self):
        """Application Constructor"""
        pass

    def add(self, a, b):
        """Adding two numbers"""
        try:
            total = int(a) + int(b)
            print(total)
            return total
        except:
            print("Invalid Entry. Use numbers only!!!")
            return "Invalid Entry"

    def add_multiple(self, *args):
        """Adding multiple numbers"""
        if not args:
            return "No values provided"
        total = 0
        try:
            for value in args:
                total += int(value)
            return total
        except Exception as e:
            print(e)
            return "Invalid Values"

    def multiple_operations(self, a, b, sign):
        try:
            a = int(a)
            b = int(b)
            if sign == "+":
                return a + b
            elif sign == "*":
                return a*b
            elif sign == "-":
                return a-b
            else:
                return "Unsupported Operation"
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
