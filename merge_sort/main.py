def merge_sort(A):
    n = len(A)
    if (n < 2):
        return A
    
    split = int(n / 2)
    first = A[:split]
    second = A[split:]

    return merge(merge_sort(first), merge_sort(second))

def merge(A, B):
    result = []
    i = 0
    j = 0
    while (i < len(A) and j < len(B)):
        a = A[i]
        b = B[j]
        if a < b:
            result.append(a)
            i += 1
        else:
            result.append(b)
            j += 1

    if (i == len(A)):
        result.extend(B[j:])
    if (j == len(B)):
        result.extend(A[i:])

    return result