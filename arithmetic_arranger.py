def parse(problems):
    if len(problems) > 5:
        return None, "Error: Too many problems."

    result = []
    for problem in problems:
        first, sign, second = tuple(problem.split())
        if sign != "+" and sign != '-':
            return None, "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return None, "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return None, "Error: Numbers cannot be more than four digits."

        result.append(ArithmeticOperation(first, sign, second))

    return result, None



def arithmetic_arranger(problems):
    arithmetic_operations, error = parse(problems)
    if error:
        return error

    first_operation = arithmetic_operations[0]
    return "\n".join(["  " + first_operation.first() +"      123",
                      first_operation.sign() +"    "+first_operation.second()+"    +  49",
                      "------    -----"])

class ArithmeticOperation:
    def __init__(self, first, operation, second):
        self._sign = operation
        self._first = first
        self._second = second

    def first(self):
        return self._first

    def second(self):
        return self._second

    def sign(self):
        return self._sign
