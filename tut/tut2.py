class Rational:
    n = 0
    d = 1
    def __init__(a,b):
        n = abs(a)/gcd(a,b)
        d = abs(b)/gcd(a,b)
    def gcd(a,b):
        if b==0:
            return a
        else gcd(b,a%b)
    def __add__(self, inputOperand):
        return Rational(self.n*inputOperand.d+self.d*inputOperand.n,inputOPerand.n*inputOperand.d)