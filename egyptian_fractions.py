import math
import sys


def generate_egyptian_fraction(nr,dr):
	"""
	This function generates the egyptian fractions by greedy method
	"""
	nr_list = []
	while nr != 0 :
		factor = math.ceil(float(dr)/float(nr))
		nr_list.append(factor)
		nr = nr*factor - dr
		dr = dr * factor
	for nos in nr_list:
		print "1/{0}".format(nos)

if __name__ == "__main__":
	generate_egyptian_fraction(int(sys.argv[1]),int(sys.argv[2]))
