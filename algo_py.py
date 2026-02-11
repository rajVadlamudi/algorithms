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

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    


def fibonacci(n):
    result = []
    for i in range(n+1):
        result.append(0 if i==0 else 1 if i==1 else result[i-1] + result[i-2])
    return result

print(fibonacci(6))  # Output: [0, 1, 1, 2, 3, 5]

def palindrome(word):
    result = False
    temp = ''
    word = word.lower()
    for i in range(len(word)-1, -1, -1):
        temp += word[i]
    if temp == word:
        result = True
    return result

print('palindrome(Madam)',palindrome('Madam'))  # Output: True
print('palindrome(none)',palindrome('none'))  # Output: True

def flatten(arr):
    result = []
    for i in arr:
        if type(i) == list:
            result.extend(i)
        else:
            result.append(i)
    return result

def sum(arr):
    result = []
    arr = flatten(arr)
    for i in range(len(arr)-1):
        result.append(arr[i] + arr[i+1])
    return result

def pascal(n):
    result = []
    for i in range(n):
        result.append(1 if i == 0 else [1,1] if i== 1 else flatten([1,sum(result[i-1]), 1]))
    return result

print(pascal(6))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]