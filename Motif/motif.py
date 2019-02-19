def u_motif(s, t):
    locations, i, j, ln = [], 0, len(t), len(s)
    while j <= ln:
        if s[i:j] == t:
            locations.append(i + 1)
        i += 1
        j += 1

    return ' '.join(str(e) for e in locations)


seq = open('rosalind_subs.txt', 'r')
print(u_motif((seq.readline()).strip(), seq.readline().strip()))
seq.close()

"""
def u_motif(s, t):
    locations, i, j, ln = [], 0, len(t) - 1, len(s)
    while j <= ln:
        wut = s[i:j]
        if wut in t:
            locations.append(i + 1)
        i += 1
        j += 1

    return ' '.join(str(e) for e in locations)


seq = open('rosalind_subs.txt', 'r')
print(u_motif(seq.readline().strip(), seq.readline()))
seq.close()
"""
