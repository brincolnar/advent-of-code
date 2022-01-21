horizontal = 0
depth = 0

with open('../input/input2.txt') as input_file:
    for line in input_file:
        direction = line.split()[0]
        amount = int(line.split()[1])

        if(direction == "forward"):
            horizontal += amount
        elif(direction == "down"):
            depth += amount
        elif(direction == "up"):
            depth -= amount

print("horizontal: " + str(horizontal))
print("depth: " + str(depth))