position = 0
depth = 0
aim = 0

input = open('input.txt').read().split('\n')
for instruction in input:
    direction, value = instruction.split()
    value = int(value)

    if direction == 'forward':
        position += value
        depth += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value

print('Part 1:', position * aim)
print('Part 2:', position * depth)