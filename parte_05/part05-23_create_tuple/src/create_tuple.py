# Write your solution here
def create_tuple(x: int, y: int, z: int):
    sort = sorted([x, y, z])
    creaTup = (sort[0], sort[-1], sum(sort))
    return creaTup
    
if __name__ == "__main__":
    create_tuple()