# //command: python algo_py.py

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # Output: 120

def sort(arr):
    result = []
    min = 0
    index = 0
    while len(arr) > 0:
        index = 0
        min = arr[index]
        for i in range(1, len(arr)):
            if arr[i] < min:
                index = i
                min = arr[i]
        result.append(min)
        arr.pop(index)

    return result

test = [4,5,3,1,2]
print(sort(test))

