def reproduce(fishes, days):
    return sum([repro(days - fish - 1) + 1 for fish in fishes])

def repro(days, cache = {}):
    if days in cache:
        return cache[days]
    elif days < 0:
        return 0
    else:
        result = repro(days - 7, cache) + repro(days - 9, cache) + 1
        cache[days] = result
        return result

input = [int(i) for i in open('input.txt').readline().split(',')]
print('fish after 80 days: ', reproduce(input, 80))
print('fish after 256 days: ', reproduce(input, 256))