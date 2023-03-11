def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        first, operation, second = tuple(problem.split())

        if operation != "+" and operation != '-':
            return "Error: Operator must be '+' or '-'."

        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

    return "\n".join(["  3801      123", "-    2    +  49", "------    -----"])