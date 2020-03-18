import argparse
from bitarray import bitarray
from rank import rank1, rank0

'''
the primary call script for functions rank and select. 
'''

def main():

    # create a parser object
    parser = argparse.ArgumentParser(description = "A program for testing an implementation of a Bloom Filter") 
    
    # creating a map of functions that bv.py can run
    #FUNCTION_MAP = {'build'    : rankSupport,
                     'rank1'    : rankSupport,
                     'rank0'    : rankSupport,
                     'overhead' : rankSupport}
    
    parser.add_argument("command", choices = FUNCTION_MAP.keys())

    # add bv.py arguments
    #parser.add_argument()

    # parse the arguments from standard input
    args.parse_args()

    # PERFORM COMMANDS BASED ON STD. IN
    
    if args.command == "build":
        #run the build() function written in rankSupport.py

    elif args.command == "rank1":
        #run the rank1() function written in rankSupport.py
    
    elif args.command == "rank0":
        #run rank0()

    elif args.command == "overhead":
        #run overhead()

    else:
        print("The command you have entered is not one of: 'rank1', 'rank0', or 'overhead'. Please try again.")


if __name__ == "__main__":
    main() 
