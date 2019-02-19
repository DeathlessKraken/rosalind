def ACGU_count(str):
    return str.replace('T', 'U')


seq = open("rosalind_rna.txt", "r")
print(ACGU_count(seq.read()))
seq.close()
