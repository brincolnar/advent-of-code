zeros_count = [0 for i in range(12)]
ones_count = [0 for i in range(12)]

with open('./input3.txt') as input_file:

    for line in input_file:
        for i in range(len(line)):
            ith_bit = line[i]
            if(ith_bit == '0'):
                zeros_count[i] += 1
            elif(ith_bit == '1'):
                ones_count[i] += 1

gamma = ''
for i in range(len(zeros_count)):
    print('counts for ' + str(i) + 'th position: ')
    print('0s: ' + str(zeros_count[i]))
    print('1s: ' + str(ones_count[i]))

    if(zeros_count[i] > 500):
        gamma += '0'
    else:
        gamma += '1'

print('gamma: ')
print(gamma)

# epsilon is flipped gamma
epsilon = ''
for bit in gamma:
    if bit == '0':
        epsilon += '1'
    else:
        epsilon += '0'


print('epsilon: ')
print(epsilon)

# convert to decimal and multiply
product = int(gamma,2) * int(epsilon,2)
print("product: ")
print(product)