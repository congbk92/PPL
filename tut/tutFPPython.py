def double1(lst):
	return [x*2 for x in lst]
def double2(lst):
	return [lst[0]*2] + double2(lst[1:]) if lst else []
def double3(lst):
	return list(map(lambda x:x*2,lst))
print(double1([5,7,12,-4]))
print(double2([5,7,12,-4]))
print(double3([5,7,12,-4]))

def flatten(lst)
	return [x*2 for x in [y for y in lst]]

print(flatten([1,2,3],[’a’,’b’,’c’],[1.1,2.1,3.1]))