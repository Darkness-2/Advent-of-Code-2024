class Equation:
    target = 0
    operands: list[int] = []

    def __init__(self, target: int, operands: list[int]):
        self.target = target
        self.operands = operands
