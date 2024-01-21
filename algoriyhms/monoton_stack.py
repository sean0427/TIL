def monoton(A):
    s = []
    result = [-1] * len(A)

    for idx, v in enumerate(A):
        while s and A[s[-1]] > v:
            s.pop()
            result[idx] = s[-1]
        else:
            result[idx] = -1
        s.append(idx)

    return result


if __init__ == '__main__':
    A = [3, 7, 8, 4]
    result = monoton(A)
    print(result)


