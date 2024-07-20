# Write your solution here

def histogram(string: str):
    worDict = {}
    for letter in string:
        if letter not in worDict:
            worDict[letter] = "*"
        else:
            worDict[letter] += "*"
    for key, value in worDict.items():
        print(key, value)
    
if __name__ == "__main__":
    histogram()