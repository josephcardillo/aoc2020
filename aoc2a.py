import re # https://docs.python.org/3/library/re.html#re.split

# Part 1

def validate(lines):
    valid_pw_count = 0 # Start counter at zero
    for line in lines:
        stripped = line.replace(': ', ' ').replace('-', ' ').strip()
        arr = (re.split('\s+', stripped))
        # For readability, set each to a variable
        smallest = int(arr[0])
        highest = int(arr[1])
        letter = arr[2]
        password = arr[3]
        frequency = int(password.count(letter))
        if smallest <= frequency <= highest:
            # Print statement so I can see what's actually going on.
            print(f"{letter} occurs {frequency} number of times and is valid password.")
            valid_pw_count += 1
            print(f"Valid password count is: {valid_pw_count}.")
        elif frequency < smallest or frequency > highest:
            print(f"{letter} occurs {frequency} number of times and is invalid password.")
        print(valid_pw_count)

with open('aoc2a.txt', 'r') as f:
    lines = f.readlines()

validate(lines)