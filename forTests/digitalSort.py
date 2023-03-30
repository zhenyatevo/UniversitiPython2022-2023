def digitalSort(arr):
    try:
        if arr == []:
            return []
        else:
            for c in arr:
                if type(c) is float or type(c) is str:
                    raise ValueError()

            max_digit = len(str(max(arr)))
        #res=[]
        for i in range(max_digit):
            buckets = [[] for _ in range(10)]
            for num in arr:
                digit = num // (10 ** i) % 10
                buckets[digit].append(num)
            arr = [num for bucket in buckets for num in bucket]
            #res.append(arr)
        #return res
        return arr
    except (ValueError, TypeError):
                raise ValueError("Выражение на вход должно являться массивом целых чисел")

if __name__ == "__main__":
    print(digitalSort([100, 3, -56, 8]))