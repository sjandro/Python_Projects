import sys

def mult(x, y):
	product = 0
	for i in range(y):
		product += x
	return product

print(str(mult(int(sys.argv[1]),int(sys.argv[2]))))