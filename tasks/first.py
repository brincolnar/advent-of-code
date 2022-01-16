import sys

num_increased = 0

with open('./input1.txt') as input_file:
    previous = "(N/A - no previous measurement)"
    for line in input_file:
        current = int(line)

        if(previous == "(N/A - no previous measurement)"): # first line
            previous = current
        else: 
            if(previous < current):
                num_increased += 1
                print("current")
                print(current)
                print("previous")
                print(previous)
            previous = current
        

print("num_increased: ")
print(num_increased)