class Expr():
	pass

class Var(Expr):
	def __init__(self,name):
		self.name = name
	def eval(self):
		return Number(1)
class Number(Expr):
	def __init__(self,n):
		self.n = n
	def print(self):
		print(self.n)
	def eval(self):
		return self

class UnOp(Expr):
	def __init__(self,operator,arg):
		self.operator = operator
		self.arg = arg
	def eval(self):
		return Number(-self.arg)
class BinOp(Expr):
	def __init__(self,left,operator,right):
		self.operator = operator
		self.left = left
		self.right = right
	def eval(self)
		
v = Var("x")
BinOp(Number(0.2),"+",v)
