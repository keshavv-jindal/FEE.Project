def average(array):
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = int(sum_array/len_array)
    return output
    
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
