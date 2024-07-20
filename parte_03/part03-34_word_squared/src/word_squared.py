# Write your solution here
def squared(word, value):
    index = 0
    count = 0
    word *= value * value
    while count < value:
        print(word[index:index+value])
        index += value
        count += 1

if __name__ == "__main__":
    squared("python", 15)