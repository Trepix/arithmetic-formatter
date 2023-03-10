def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        first, operation, second = tuple(problem.split())

        if operation != "+" and operation != '-':
            return "Error: Operator must be '+' or '-'."

    return None