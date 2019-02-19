def RC(str):
    a = list(str)
    a.reverse()
    for l in range(len(a)):
        if a[l] == 'A':
            a[l] = 'T'
        elif a[l] == 'T':
            a[l] = 'A'
        elif a[l] == 'G':
            a[l] = 'C'
        elif a[l] == 'C':
            a[l] = 'G'

    return ''.join(a)


seq = open("rosalind_revc.txt", "r")
print(RC(seq.read()))
seq.close()
