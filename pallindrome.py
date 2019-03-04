import math

def generate_pallindrome(n,odd):
"""
This function is used to generate pallindrome numbers for a particular number n by appending
the reverse if the pallindrome number contains even number of digits and by dropping the last digit and then appending the rest
if the pallindrome number contains odd number of digits
"""
	palindrome_no = n
	digit = 0
	if odd:
		n/=10
	while n>0:
		palindrome_no = palindrome_no*10+(n%10)
		n /= 10
	return palindrome_no

def find_pallindromes_and_calculate_sum(n):
"""
This function generates all the pallindrome numbers, checks if the generated numbers are pallindrome in binary also and then
finally calculates the sum
"""
	odd_values = [True, False]
	sum = 0
	for odd in odd_values:
		for i in range(0,int(math.sqrt(n))):
			palindrome_no = generate_pallindrome(i, odd)
			if palindrome_no < n and check_if_binary_pallindrome(palindrome_no):
				sum += palindrome_no
	print sum	

def check_if_binary_pallindrome(m):
"""
this function checks if the binary version of the number is pallindrome or not.
"""
	str_b = "{0:b}".format(m)
	l = 0
	r = len(str_b)-1
	while (l<r):
		if (str_b[l] != str_b[r]):
			return False
		else:
			pass
		l+=1
		r-=1
	return True

find_pallindromes_and_calculate_sum(1000000)
