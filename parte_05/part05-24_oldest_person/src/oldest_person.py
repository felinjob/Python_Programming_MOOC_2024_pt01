# Write your solution here
def oldest_person(people: list):
    oldest = []
    for person in people:
        oldest.append(person[1])
    oldest = min(oldest)
    for person in people:
        if oldest == person[1]:
            return person[0]
    
    
if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    
    print(oldest_person(people))