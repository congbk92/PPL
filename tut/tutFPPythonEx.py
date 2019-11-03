def double1(lst):
	return [x*2 for x in lst]
def double2(lst):
	return [lst[0]*2] + double2(lst[1:]) if lst else []
def double3(lst):
	return list(map(lambda x:x*2,lst))
print(double1([5,7,12,-4]))
print(double2([5,7,12,-4]))
print(double3([5,7,12,-4]))

def flatten1(lst):
	return [ele for item in (x for x in lst) for ele in item]
def flatten2(lst):
	return lst[0] + flatten2(lst[1:]) if lst else []
import functools
def flatten3(lst):
	return list(functools.reduce(lambda a,b : a+b,lst))

print(flatten1([[1,2,3],['a','b','c'],[1.1,2.1,3.1]]))
print(flatten2([[1,2,3],['a','b','c'],[1.1,2.1,3.1]]))
print(flatten3([[1,2,3],['a','b','c'],[1.1,2.1,3.1]]))

def lessThan1(n, lst):
	return [x for x in lst if x < n]
def lessThan2(n, lst):
	if lst:
		if (lst[0] < n):
			return [lst[0]] + lessThan2(n,lst[1:])
		else:
			return [] + lessThan2(n,lst[1:])
	else:
		return []

def lessThan3(n, lst):
	return list(filter(lambda x: x < n, lst))
print(lessThan1(50, [1, 55, 6, 2]))
print(lessThan2(50, [1, 55, 6, 2]))
print(lessThan3(50, [1, 55, 6, 2]))