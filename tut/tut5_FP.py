
def double_a(lst):
	return [x*2 for x in lst]
def double_b(lst):
	return [lst[0]*2] + double_b(lst[1:]) if lst else []
def double_c(lst):
	return list(map(lambda x:x*2, lst))
lst = [5,7,12,-4]
print(double_a(lst))
print(double_b(lst))
print(double_c(lst))

def flatten_a(lst):
	return [x for sublist in lst for x in sublist]
def flatten_b(lst):
	return lst[0] + flatten_b(lst[1:]) if lst else []
import functools 
def flatten_c(lst):
	return functools.reduce(lambda a,b: a+b, lst)
lst = [1,2,3],['a','b','c'],[1.1,2.1,3.1]
print(flatten_a(lst))
print(flatten_b(lst))
print(flatten_c(lst))

def lessThan_a(n,lst):
	return [x for x in lst if x < n]
def lessThan_b(n,lst):
	return [] if not lst else [] + lessThan_b(n,lst[1:]) if lst[0] >= n else [lst[0]] + lessThan_b(n,lst[1:])
def lessThan_c(n,lst):
	return list(filter(lambda x: x < n, lst))

lst = [1, 55, 6, 2]
n = 50
print(lessThan_a(n,lst))
print(lessThan_b(n,lst))
print(lessThan_c(n,lst))