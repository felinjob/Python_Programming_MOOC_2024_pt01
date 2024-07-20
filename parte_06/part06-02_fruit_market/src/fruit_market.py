# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        market = {}
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            key = parts[0]
            values = float(parts[1])
            market[key] = values
        return market
    
if __name__ == "__main__":
    read_fruits()