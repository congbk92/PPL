class rational:
    def __init__(self,inN=0,inD=1):
        self.n = inN
        self.d = inD
        g = 1
        g = self.gcd(abs(self.n),abs(self.d))
        self.number = int(self.n/g)
        self.denom = int(self.d/g)
        
    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b,a%b)
    def __add__(self,other):
        if type(other) is int:
            return self + rational(other)
        else:
            return rational(self.number*other.denom + self.denom*other.number, self.denom*other.denom)
        
    def __str__(self):
        return "{0}/{1}".format(self.number,self.denom)

print(rational(25,100)+rational() + 4)