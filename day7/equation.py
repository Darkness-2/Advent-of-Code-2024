from itertools import product
from typing import Iterable, Literal


type Operator = Literal['+', '*', '||']


class Equation:
    target = 0
    operands: list[int] = []

    def __init__(self, target: int, operands: list[int]):
        self.target = target
        self.operands = operands

    def test_equation(self, operators: Iterable[Operator]) -> bool:
        # TODO: Replace with recursive function that checks last operand first

        # For each permutation, perform the calculation
        for perm in product(operators, repeat=len(self.operands) - 1):
            running_calc = self.operands[0]
            for i, operator in enumerate(perm):
                match operator:
                    case '+':
                        running_calc += self.operands[i + 1]
                    case '*':
                        running_calc *= self.operands[i + 1]
                    case '||':
                        running_calc = int(
                            str(running_calc) + str(self.operands[i + 1]))

            if running_calc == self.target:
                return True

        return False
