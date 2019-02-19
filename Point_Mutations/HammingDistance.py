def ham(str1, str2):
    counter = 0
    for x in range(len(str1)):
        if str1[x] != str2[x]:
            counter += 1
    return counter


seq = open('rosalind_hamm.txt', 'r')
print(ham(seq.readline(), seq.readline()))
seq.close()
