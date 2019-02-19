def RNATrans(s, d):
    i, j, ln = 0, 3, len(s)
    result = ""
    while j <= ln:
        if d[s[i:j]] == "Stop":
            break
        result += d[s[i:j]]
        i += 3
        j += 3

    return result


seq = open("rosalind_prot.txt", "r")
table = open("RNA_codon_table.txt", "r")

line = table.readline().strip()
line = line.split()
codon_table = {}

while line:
    codon_table[line[0]] = line[1]
    line = table.readline().strip()
    line = line.split()

print(RNATrans(seq.readline().strip(), codon_table))
seq.close()
table.close()
