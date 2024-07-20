# Write your solution here
import string
def change_case(orig_string: str) -> str:
    return orig_string.swapcase()
    
    
def split_in_half(orig_string: str) -> str:
    if len(orig_string) % 2 != 0:
        part1 = orig_string[:len(orig_string) // 2]
        part2 = orig_string[len(orig_string) // 2:]
        return part1, part2
    if len(orig_string) % 2 == 0:
        part1 = orig_string[:len(orig_string) // 2]
        part2 = orig_string[len(orig_string) // 2:]
        return part1, part2
    
def remove_special_characters(orig_string: str) -> str:
    new_orig = ""
    for letter in orig_string:
        if letter in string.ascii_letters or letter in string.digits or letter == " ":
            new_orig += letter
    return new_orig