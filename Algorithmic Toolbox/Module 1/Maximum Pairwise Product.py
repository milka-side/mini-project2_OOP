import ctypes


n = int(input())
arr_type = ctypes.py_object * n
arr = arr_type()
numbers = list(map(int, input().split()))
for i in range(n):
    arr[i] = numbers[i]
max1, max2 = -1, -1
for i in range(n):
    if arr[i] > max1:
        max2, max1 = max1, arr[i]
    elif arr[i] > max2:
        max2 = arr[i]
print(max1 * max2)
