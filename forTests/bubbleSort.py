#m = list(map(int, input().split(" ")))
def bubbleSort(m):
    try:
        for i in range(0, len(m)-1):
            buf = 1000
            #res=[]
            for j in range(0, len(m)-1):
                if m[j+1] < m[j]:
                    buf = m[j]
                    m[j] = m[j+1]
                    m[j+1] = buf
                #res.append(m)
        #return res
        return m
    except (ValueError, TypeError):
                raise ValueError("Выражение на вход должно являться массивом")


if __name__ == "__main__":
    print(bubbleSort([100, 3, -56, 8]))