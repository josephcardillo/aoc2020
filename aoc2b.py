import re # https://docs.python.org/3/library/re.html#re.split

# Part 2

def validate(lines):
    valid_pw_count = 0 # Start counter at zero
    for line in lines:
        stripped = line.replace(': ', ' ').replace('-', ' ').strip()
        arr = (re.split('\s+', stripped))
        # For readability, set each to a variable
        first = int(arr[0]) - 1
        second = int(arr[1]) - 1
        letter = arr[2]
        password = arr[3]
        first_char = arr[3][first]
        second_char = arr[3][second]
        if first_char == letter and second_char != letter:
            print(f"{password} is valid.")
            valid_pw_count += 1
        elif first_char != letter and second_char == letter:
            print(f"{password} is valid.")
            valid_pw_count += 1
        else:
            print(f"{password} is invalid")
    print(valid_pw_count)

with open('aoc2a.txt', 'r') as f:
    lines = f.readlines()

validate(lines)