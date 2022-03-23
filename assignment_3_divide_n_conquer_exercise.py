print("\n---------Problem Statement - Polynomial Multiplication-----------\n")

"""
Solution:
1. Get the length of both the list poly_a and poly_b
2. Get the product length of poly_a and poly_. formula is: prod_len = len(poly_a) + len(poly_b) -1
3. Create an list of 0s from the product length (product).
4. product[poly_a_index+poly_b_index] = Sum of all the pairs poly_a[poly_a_index] * poly_b[poly_b_index]
"""

def multiply_basic(poly_a, poly_b):
    product = []
    poly_a_len = len(poly_a) 
    poly_b_len = len(poly_b)
    prod_len = poly_a_len + poly_b_len - 1 # length of output, sum of 2 poly -1

    # populate the product with prod_lenght so we can access the index
    # else we will get IndexError: list index out of range
    product = [0] * prod_len

    # here each element from the poly_a will multiply with poly_b element and the 
    for poly_a_index in range(poly_a_len): # this will get one index to multiply with all of poly_b_len
        for poly_b_index in range(poly_b_len): # this will be multiplyed by all the indexed elements of poly_a_len
            # add the multiplication at the sum of the integers index
            # ex: product[0] = 2*3, product[1] = 2*4, product[2] = (2*2)+(5*2)
            product[poly_a_index+poly_b_index] += poly_a[poly_a_index] * poly_b[poly_b_index]

    return product

print("Polynomial of [2, 0, 5, 7], [3, 4, 2]: ",multiply_basic([2, 0, 5, 7], [3, 4, 2])) # 4 * 3 = O(n-1)^2
print()
print("Polynomial of [3,2,1], [4,0,3,-1]: ",multiply_basic([3,2,1], [4,0,3,-1])) # 3 * 4 = O(n+1)^2
print()
print("Polynomial of [4,3,2,1], [1,2,3,4]: ",multiply_basic([4,3,2,1], [1,2,3,4])) # 4 * 4 = O(n)^2
print()
print("Polynomial of [0], [0]: ",multiply_basic([0], [0])) 
print()
print("Polynomial of [1], [0]: ",multiply_basic([1], [0])) 
print()
print("Polynomial of [1], [1]: ",multiply_basic([1], [1])) 

# conquer
def add(poly_a, poly_b):
    """Add two polynomials"""
    result = [0] * max(len(poly_a), len(poly_b))
    for i in range(len(result)):
        if i < len(poly_a):
            result[i] += poly_a[i]
        if i < len(poly_b):
            result[i] += poly_b[i]
    return result

# divide 
def split(poly_a, poly_b):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly_a), len(poly_b)) // 2
    return  (poly_a[:mid], poly_a[mid:]), (poly_b[:mid], poly_b[mid:])

# this is to create n times list of 0 and add the poly list to it.
# So the exponent (x^n) will increase by n.
def increase_exponent(poly, n):
    """Multiply poly_a by x^n"""
    return [0] * n + poly

def multiply_optimized(poly_a, poly_b):
    # get length of lists
	len_a,len_b = len(poly_a),len(poly_b)
    # if both list are empty 
	if len_a == 0 and len_b == 0:
		return [0]
    # if either of the list are empy retrun the max list of lists
	if len_a == 0 or len_b == 0:
		return [0] * max(len_a,len_b)
    # multiply first element of poly_a with all of poly_b and retrun list
	if len_a == 1:
		return [poly_a[0] * poly_b[i] for i in range(len_b)]
    # multiply first element of poly_b with all of poly_a and retrun list
	elif len_b == 1:
		return [poly_b[0] * poly_a[i] for i in range(len_a)]
    # if both have lenght > 1, get the max length of both lists
	else:
		n = max(len_a,len_b)
		
    # split the lists to have equal 4 lists
	(A0, A1), (B0, B1) = split(poly_a, poly_b)

	# divide and conqure
	Y = multiply_optimized(add(A0,A1), add(B0,B1))
	U = multiply_optimized(A0, B0)
	Z = multiply_optimized(A1, B1)

    # U + [Y - U - Z]n//2 + [Z]2*(n//2)
    # There are 3 additions and 2 increase_exponent
	result = add(add(U, increase_exponent(add(Y, [-x for x in add(U,Z)]), n//2)), increase_exponent(Z,2*(n//2)))

	return result

print()
print("Polynomial D&C of [2, 0, 5, 7], [3, 4, 2]: ",multiply_optimized([2, 0, 5, 7], [3, 4, 2])) # 4 * 3 = O(n-1)^2
print()
print("Polynomial D&C of [3,2,1], [4,0,3,-1]: ",multiply_optimized([3,2,1], [4,0,3,-1])) # 3 * 4 = O(n+1)^2
print()
print("Polynomial D&C of [4,3,2,1], [1,2,3,4]: ",multiply_optimized([4,3,2,1], [1,2,3,4])) # 4 * 4 = O(n)^2
print()
print("Polynomial D&C of [0], [0]: ",multiply_optimized([0], [0])) 
print()
print("Polynomial D&C of [1], [0]: ",multiply_optimized([1], [0])) 
print()
print("Polynomial D&C of [1], [1]: ",multiply_optimized([1], [1])) 