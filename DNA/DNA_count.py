def ACGT_count(str):
    a = list(str)
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return '{} {} {} {}'.format(d['A'], d['C'], d['G'], d['T'])


seq = open('rosalind_dna.txt', 'r')
print(ACGT_count(seq.read()))
seq.close()
