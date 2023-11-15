def calculate(left, right, operation):
    # show match case: https://www.geeksforgeeks.org/python-match-case-statement/
    # match params:
    #     case first:
    #     case second:
    #     case _
    res = 0
    if operation == "+":
        res = left + right
    elif operation == "-":
        res = left - right
    elif operation == "/":
        try:
            res = left / right
        except ZeroDivisionError:
            print("Right is 0, can not delete")
            return None
    elif operation == "*":
        res = left * right
    else:
        print("Unknown operation")
    return res
