def digitalSort(arr):
    max_digit = len(str(max(arr)))
    res=[]
    for i in range(max_digit):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = num // (10 ** i) % 10
            buckets[digit].append(num)
        arr = [num for bucket in buckets for num in bucket]
        res.append(arr)
    return list(res)

arr = list(map(int,input().split(" ")))
result = digitalSort(arr)
for i in range (0,len(result)):
    print(*result[i])