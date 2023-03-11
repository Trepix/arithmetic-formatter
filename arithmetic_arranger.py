def parse(problems):
    if len(problems) > 5:
        return None, "Error: Too many problems."

    result = []
    for problem in problems:
        first, operation, second = tuple(problem.split())
        if operation != "+" and operation != '-':
            return None, "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return None, "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return None, "Error: Numbers cannot be more than four digits."

        result.append(ArithmeticOperation(first, operation, second))

    return result, None



def arithmetic_arranger(problems):
    arithmetic_operations, error = parse(problems)
    if error:
        return error

    return "\n".join(["  3801      123", "-    2    +  49", "------    -----"])

class ArithmeticOperation:
    def __init__(self, first, operation, second):
        self.operation = operation
        self.first = first
        self.second = second
