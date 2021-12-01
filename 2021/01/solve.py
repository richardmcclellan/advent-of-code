def numIncreases(arr):
    sum = 0
    for i in range(1, len(arr)):
        if (arr[i] > arr[i - 1]):
            sum+=1
    return sum

def movingAverageNumIncreases(arr, k=3):
    sum = 0
    nextSum = 0
    numIncreases = 0
    
    for i in range(len(arr)):
        if i < k:
            sum += arr[i]
        else:
            nextSum = sum + arr[i] - arr[i-k]
            if nextSum > sum: 
                numIncreases += 1
            sum = nextSum
        
    return numIncreases

input = [int(value) for value in open('input.txt').read().split()]
print("input length:" + str(len(input)))
print("Num increases: " + str(numIncreases(input)))
print("Num moving average increases: " + str(movingAverageNumIncreases(input)))