from scipy.special import comb


class Drv(object):
    """
    Define a class for discrete random variable

    xk is a list of monoton increasing values
    pk is the list of probabilities belonging to xk
    """

    def __init__(self, xk: list, pk: list):
        self.xk = xk
        self.pk = pk

    def pdf(self, x: int) -> int:
        for i in range(len(self.xk)):
            if self.xk[i] == x:
                return self.pk[i]

    def cdf(self, x: int) -> float:
        res = 0
        i = 0
        if x > self.xk[-1]:
            return 1.0
        else:
            while x > self.xk[i]:
                res += self.pk[i]
                i += 1

        return res

    def e(self) -> float:
        """
        Return the expected value of the discrete random variable.
        """
        # return here the value
        return sum([x * y for x, y in zip(self.xk, self.pk)])

    def is_nonneg(self) -> bool:
        """
        Return True if the random variable is non negative.
        Otherwise False.
        """
        # return here True or False
        for x in self.xk:
            if x < 0:
                return False

        return True

    def reweight(self):
        """
        Reweighting a random variable using the expected
        value of the random variable.
        """
        # write the code here
        weight = [x * y / self.e() for x, y in zip(self.xk, self.pk)]
        return Drv(self.xk, weight)


class Binomial(Drv):
    """
    Class for binomial random variable derives from Drv.
    Parameters needed: n, p.
    """

    def __init__(self, n: int, p: float):
        self.n = n
        self.p = p
        # define the values and probabilities of the binomial variable here
        super().__init__(list(range(0, n+1)), [self.binom_pmf(i) for i in range(self.n)])  # inheritance

    def binom_pmf(self, i: int) -> int:
        return comb(self.n, i) * self.p**i * (1 - self.p)**(self.n - i)

    def e(self) -> float:
        """
        Return the expected value of the binomial random variable.
        """
        # return the value here
        return self.n * self.p


class Uniform(Drv):
    """
    Class for a uniform random variable derives from Drv.
    n:   the number a values (which are 1,2,...,n)
    """

    def __init__(self, n):
        self.n = n
        # define the values and probabilities of the uniform variable here
        # and complete the code
        super().__init__(list(range(1, n+1)), [1 / self.n] * self.n)

    def e(self) -> float:
        """
        Return the expected value of the uniform random variable.
        """
        # return the value here
        return (self.n + 1) / 2
