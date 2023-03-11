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

def space(iterable):
    return "    ".join(iterable)
def arithmetic_arranger(problems):
    arithmetic_operations, error = parse(problems)
    if error:
        return error

    return "\n".join([space(map(ArithmeticOperation.first_line, arithmetic_operations)),
                      space(map(ArithmeticOperation.second_line, arithmetic_operations)),
                      space(map(ArithmeticOperation.equal_line, arithmetic_operations))])

class ArithmeticOperation:
    def __init__(self, first_number, operation, second_number):
        self._sign = operation
        self._first_number = first_number
        self._second_number = second_number
        longest_digits = max(len(first_number), len(second_number))
        self.total_characters = longest_digits + len(self._sign) + 1

    def _first_whitespaces(self):
        return self.total_characters - len(self._first_number)
    def first_line(self):
        return " " * self._first_whitespaces() + self._first_number

    def _second_whitespaces(self):
        return self.total_characters - len(self._second_number) - len(self._sign)
    def second_line(self):
        return self._sign + " "* self._second_whitespaces() + self._second_number

    def equal_line(self):
        return "-" * self.total_characters
