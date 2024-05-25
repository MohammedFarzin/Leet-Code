n = 2
def isHappy(  n: int) -> bool:
	#20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
	slow =  squared(n)
	fast =  squared( squared(n))

	while slow!=fast and fast!=1:
		slow =  squared(slow)
		fast =  squared( squared(fast))

	return fast==1

def squared(  n):
	result = 0
	while n>0:
		last = n%10
		result += last * last
		n = n//10
	return result


print(isHappy(n))