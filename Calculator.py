class Caalculator:
    def __init__(self) -> None:

        pass

    def add(self, x1, x2) -> float:
        print("Adding..", x1, x2)
        n = max(len(str(x1 % 10)) - 2, len(str(x2 % 10)) - 2)
        answer = round(x1 + x2, n)

        return answer

    def subtract(self, x1, x2) -> float:
        n = max(len(str(x1 % 10)) - 2, len(str(x2 % 10)) - 2)
        answer = round(x1 - x2, n)

        return answer

    def multiply(self, x1, x2) -> float:
        n = len(str(x1 % 10)) - 2 + len(str(x2 % 10)) - 2
        answer = round(x1 * x2, n)

        return answer

    def divide(self, x1, x2) -> float:
        n = max(len(str(x1 % 10)) - 2, len(str(x2 % 10)) - 2)
        answer = round(x1 / x2, n)

        return answer
