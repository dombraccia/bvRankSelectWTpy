import something

'''
[description]
'''

# define rank methods (rank1, rank0, overhead)

class rankSupport:
    # define datamembers

    # constructor function
    def __init__(self, arg1, ...):
        
        # initializing datamembers from standard input
        #do some stuff here

    # define methods (public or private) to run on the rankSupport class just defined

    # define build method
    def build(self, N, pct_populated):
        #write a build function that creates a bitvector of size N bits and has pct_populated % of its elements populated with 1's

    def rank1(i):
	#write rank1 so that it returns the number of 1's up to and including element i

    def rank0(i):
	#write rank0 so that it returns the number of 0's up to and including element i

    def overhead():
	# write overhead so that it returns the size of the rankSupport data structure (in bits) that is required to support const. time rank on a bitvector.
