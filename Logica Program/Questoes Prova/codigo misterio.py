def misterio1(v, n):
    while n>1:
        m = misterio2(v, n)
        misterio3(v, n-1, m)
        n -= 1
    return

def misterio2(v, n):
    m = 0
    i = 1
    while i<n:
        if v[i] > v[m]:
            m = i
        i += 1
    return m

def misterio3(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
    return
