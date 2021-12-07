def fuel(input, position, constantRate):
    fuel = sum([abs(val - position) if constantRate else cost(abs(val - position)) for val in input])
    return fuel

cache = {}
def cost(distance):
        if distance not in cache: 
            cache[distance] = sum([i for i in range(1, distance + 1)])
        return cache[distance]

def minFuel(input, constantRate):
    fuelToPositionMap = dict([(fuel(input, val, constantRate), val) for val in range(min(input), max(input))])
    return min(list(fuelToPositionMap.keys()))

input = [int(i) for i in open('input.txt').readline().split(',')]

print('Part 1:', minFuel(input, True))
print('Part 2:', minFuel(input, False))