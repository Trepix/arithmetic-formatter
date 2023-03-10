def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        first, operation, second = tuple(problem.split())

        if operation != "+" and operation != '-':
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if int(first) > 9999 or int(second) > 9999:
            return "Error: Numbers cannot be more than four digits."

    return None