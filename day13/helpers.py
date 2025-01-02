class Game:
    a_x = -1
    a_y = -1
    b_x = -1
    b_y = -1
    prize_x = -1
    prize_y = -1

    def __init__(self, a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]):
        self.a_x, self.a_y = a
        self.b_x, self.b_y = b
        self.prize_x, self.prize_y = prize

    def __repr__(self) -> str:
        return f"A: X+{self.a_x}, Y+{self.a_y}; B: X+{self.b_x}, Y+{self.b_y}; Prize: X={self.prize_x}, Y={self.prize_y}"

    def apply_cramers_rule(self):
        """
        Based on a system of two equations, finds a solution for x and y.

        x = button presses on button a
        y = button presses on button b

        a_x * x + b_x * y = prize_x
        a_y * x + b_y * y = prize_y

        Returns two tuples. The first are the x, y values, the second are the remainders.

        https://www.1728.org/cramer.htm
        """
        a = self.a_x
        b = self.b_x
        c = self.a_y
        d = self.b_y
        e = self.prize_x
        f = self.prize_y

        dn = (a * d) - (c * b)

        x, r_x = divmod((e * d) - (f * b), dn)
        y, r_y = divmod((a * f) - (c * e), dn)

        return (x, y), (r_x, r_y)
