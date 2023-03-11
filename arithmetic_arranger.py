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
    second_operation = arithmetic_operations[1]
    return "\n".join(["    ".join([first_operation.first(), second_operation.first()]),
                      "    ".join([first_operation.sign() + first_operation.second(), second_operation.sign() + second_operation.second()]),
                      "------    -----"])

class ArithmeticOperation:
    def __init__(self, first, operation, second):
        self._sign = operation
        self._first = first
        self._second = second
        longest_digits = max(len(first), len(second))
        self.total_characters = longest_digits + len(self._sign) + 1

    def _first_whitespaces(self):
        return self.total_characters - len(self._first)
    def first(self):
        return " " * (self.total_characters - len(self._first)) + self._first

    def _second_whitespaces(self):
        return self.total_characters - len(self._second) - len(self._sign)
    def second(self):
        return " " * self._second_whitespaces() + self._second

    def sign(self):
        return self._sign
