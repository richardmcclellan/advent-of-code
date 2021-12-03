def powerConsumption(arr):
    gamma = ''
    epsilon = ''

    for i in range(len(arr[0])):
        zeros = 0
        ones = 0
        for value in arr:
            if value[i] == '0':
                zeros += 1
            elif value[i] == '1':
                ones += 1

        if(zeros > ones):
            gamma += '0'
            epsilon += '1'
        elif(ones > zeros):
            gamma += '1'
            epsilon += '0'

        gammaDecimal = b2d(gamma)
        epsilonDecimal = b2d(epsilon)

    return gammaDecimal * epsilonDecimal

def lifeSupportRating(arr):
    oxy = find(arr, 0, True)
    co2 = find(arr, 0, False)
    return b2d(oxy) * b2d(co2)


def find(arr, index, mostCommon):
    zeros = []
    ones = []
    for value in arr:
        if(value[index] == '0'):
            zeros.append(value)
        elif(value[index] == '1'):
            ones.append(value)

    onesAreMostCommon = len(ones) >= len(zeros)
    if (onesAreMostCommon ^ mostCommon): # xor with mostCommon to flip the result if we want the least common
        filtered = ones
    else:
        filtered = zeros

    if(len(filtered) == 1):
        return filtered[0]
    else:
        return find(filtered, index + 1, mostCommon)


def b2d(bin):
    return int(bin, 2)

input = open('input.txt').read().split()
print('power consumption:', powerConsumption(input))
print('life support: ', lifeSupportRating(input))