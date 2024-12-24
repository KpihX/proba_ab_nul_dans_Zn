from sympy import totient, primerange

""" Functions to evaluate the probabilty of having ab = 0 for (a, b) in (Z/nZ)^2 """

""" Function to calculate directly the probability of having ab = 0 for (a, b) in (Z/nZ)^2 """

def pro_null_pairs(n):
    count = 0
    for a in range(n):
        for b in range(n):
            if (a * b) % n == 0:
                count += 1
    return count / n ** 2

""" Function to calculate that probability using the sum formula : $\sum_{d|n} \frac{\mu(d)}{d^2}$ """

def sum_formula(n):
    result = 0
    for d in range(1, n + 1):
        if n % d == 0:
            result += totient(d) / d
    return float(result/n)

""" Function to calculate that probability using the product formula : 
$\prod_{k=1}^{m} \frac{p_k \cdot (\alpha_k + 1) - \alpha_k}{p_k^{\alpha_k + 1}}$ où $n = \prod_{k=1}^{m} p_k^{\alpha_k}$
"""

def prod_formula(n):
    factors = factorize(n)
    result = 1
    for p, alpha in factors.items():
        result *= (p * (alpha + 1) - alpha) / (p ** (alpha + 1))
    return result

# Function to factorize a number into its prime factors
def factorize(n):
    factors = {}
    for p in primerange(1, n + 1):
        alpha = 0
        while n % p == 0:
            n //= p
            alpha += 1
        if alpha > 0:
            factors[p] = alpha
    return factors

""" Functions to evaluate the probabilty that a1...ak = 0 for (a1, ..., ak) in (Z/nZ)^k """

""" Function to calculate directly the probability of having a1...ak = 0 for (a1, ..., ak) in (Z/nZ)^k """

def pro_null_k(n):
    pass

""" Function to calculate that probability using the sum formula : ??? $\sum_{d|n} \frac{\mu(d)}{d^2}$ ??? """

def sum_formula_k(n):
    pass

""" Function to calculate that probability using the product formula : ???
$\prod_{k=1}^{m} \frac{p_k \cdot (\alpha_k + 1) - \alpha_k}{p_k^{\alpha_k + 1}}$ où $n = \prod_{k=1}^{m} p_k^{\alpha_k}$
???
"""

def prod_formula_k(n):
    pass