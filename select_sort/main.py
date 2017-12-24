def select_sort(A):
    length = len(A)
    # Loop throug the list
    for i in range(0, length):
        # Find the smallest number
        imin = i
        j = i + 1
        while j <  length:
            foo = A[imin]
            bar = A[j]
            if A[j] < A[imin]:
                imin = j
            j += 1

        # Swap that smallest value with the current index
        min = A[imin]
        A[imin] = A[i]
        A[i] = min + 1
        
        i += 1

    return A