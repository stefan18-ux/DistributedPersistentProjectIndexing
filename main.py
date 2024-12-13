import sys

value_mapping = {}
level = 0

arguments = sys.argv

if len(arguments) < 2:
    print("Please provide a code to interpret!")
    exit()

input = arguments[1]
commands = []

with open(input, "r") as file:
    commands = file.readlines()
    commands = [l.strip() for l in commands]

for line in commands:
    if '{' in line:
        level += 1
    
    if '}' in line:
        for key, value in value_mapping.items():
            if len(value) and value[-1][1] == level:
                value_mapping[key].pop()
        level -= 1

    if "print" in line:
        value = line[5:]
        value = value.strip()
        # print(value_mapping[value])
        if value in value_mapping and len(value_mapping[value]):
            print((value_mapping[value])[-1][0])
            # print('\n')
        else:
            print("null")
    
    if '=' in line:
        left, right = line.split('=')
        right = right.strip()
        left = left.strip()
        if right[0] >= '0' and right[0] <= '9':
            if left not in value_mapping:
                value_mapping[left] = [[right, level]]
            else:
                if value_mapping[left][-1][1] == level:
                    value_mapping[left][-1][1] = right
                else :
                    value_mapping[left].append([right, level])
        else:
            if right in value_mapping and len(value_mapping[right]):
                if left not in value_mapping:
                    value_mapping[left] = [[value_mapping[right][-1][0], level]]
                else :
                    if value_mapping[left][-1][1] == level:
                        value_mapping[left][-1][0] = value_mapping[right][-1][0]
                    else:
                        value_mapping[left].append([value_mapping[right][-1][0], level])

    


