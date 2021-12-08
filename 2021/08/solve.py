def part1(input):
    outputs = ''.join([str(decode(line)) for line in input])
    return sum([1 for digit in outputs if digit in '1478'])

def part2(input):
    return sum([decode(line) for line in input])

def decode(line):
    patterns, outputs = line.split('|')
    patternList = [''.join(sorted(pattern)) for pattern in patterns.split()]
    outputList = [''.join(sorted(output)) for output in outputs.split()]
    key = deduceKey([pattern for pattern in patternList])
    decodedDigits = [key[output] for output in outputList]
    return sum([digit * 10 ** index for index, digit in enumerate(reversed(decodedDigits))])

def containsAll(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]

def deduceKey(patterns):
    orderedPatterns = [None] * 10
    fives = []
    sixes = []
    for pattern in patterns:
        if len(pattern) == 2:
            # 1 is the only 2 digit pattern
            orderedPatterns[1] = pattern
        elif len(pattern) == 3:
            # 7 is the only 3 digit pattern
            orderedPatterns[7] = pattern
        elif len(pattern) == 4:
            # 4 is the only 4 digit pattern
            orderedPatterns[4] = pattern
        elif len(pattern) == 5:
            fives.append(pattern)
        elif len(pattern) == 6:
            sixes.append(pattern)
        elif len(pattern) == 7:
            # 8 is the only 7 digit pattern 
            orderedPatterns[8] = pattern
    
    # 3 is the only 5 digit pattern that contains both segments of the 1
    for pattern in fives:
        if containsAll(pattern, orderedPatterns[1]):
            orderedPatterns[3] = pattern
            fives.remove(pattern)
            break
    
    # 6 is the only 6 digit pattern that does not contain all of the segments of 1
    for pattern in sixes:
        if not containsAll(pattern, orderedPatterns[1]):
            orderedPatterns[6] = pattern
            sixes.remove(pattern)
            break

    # 5 is the only 5 digit pattern which is a subset of 6
    for pattern in fives:
        if containsAll(orderedPatterns[6], pattern):
            orderedPatterns[5] = pattern
            fives.remove(pattern)
            break

    # 2 is the only remaining 5 digit pattern
    orderedPatterns[2] = fives[0]

    # 9 is the only remaining 6 digit pattern which contains all segments of 3
    for pattern in sixes:
        if containsAll(pattern, orderedPatterns[3]):
            orderedPatterns[9] = pattern
            sixes.remove(pattern)
            break

    # 0 is the only remaining 6 digit pattern
    orderedPatterns[0] = sixes[0]
    
    return dict([(pattern, index) for index, pattern in enumerate(orderedPatterns)])

input = open('input.txt').readlines()
print('Part 1:', part1(input))
print('Part 2:', part2(input))

