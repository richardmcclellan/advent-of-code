def overlaps(arr, considerDiagonals):
    counts = {}
    for line in arr:
        p1, p2 = line.split(' -> ')
        x1, y1 = [int(val) for val in p1.split(',')]
        x2, y2 = [int(val) for val in p2.split(',')]

        xStep = 1 if x1 < x2 else -1
        yStep = 1 if y1 < y2 else -1

        xRange = range(x1, x2 + xStep, xStep)
        yRange = range(y1, y2 + yStep, yStep)

        if not (considerDiagonals or x1 == x2 or y1 == y2):
            continue

        if len(xRange) > len(yRange):
            yRange = [yRange[0] for _ in range(len(xRange))]
        elif len(yRange) > len(xRange):
            xRange = [xRange[0] for _ in range(len(yRange))]

        for i in range(len(xRange)):
            key = str(xRange[i]) + ',' + str(yRange[i])
            counts[key] = counts.get(key, 0)  + 1
    
    return sum(1 for i in counts.values() if i > 1)

input = open('input.txt').readlines()
print('overlaps: ', overlaps(input, False))
print('overlaps (with diagonals): ', overlaps(input, True))