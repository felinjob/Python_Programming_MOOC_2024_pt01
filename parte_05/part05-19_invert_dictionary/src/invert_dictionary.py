# Write your solution here
def invert(dictionary: dict):
    keyList = []
    vaList = []
    for key, value in dictionary.items():
        vaList.append(value)
        keyList.append(key)
    dictionary.clear()
    for item in range(len(vaList)):
        dictionary[vaList[item]] = keyList[item]
if __name__ == "__main__":
    invert()