# Write your solution here
def longest(longest: str):
	    long = ""
	    for word in longest:
	        if len(word) > len(long):
	            long = word
	    return long
	 
if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    print(longest(strings))