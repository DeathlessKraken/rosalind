def gc(dna):
    ln, gc_amt = 0, 0
    for x in dna:
        if x == 'G' or x == 'C':
            gc_amt += 1
        ln += 1
    return float(100 * gc_amt / ln)


seq = open("rosalind_gc.txt", "r")
gc_strands = {}
info = ''
content = ''

for line in seq:
    if line.startswith('>'):
        if content:
            gc_strands[info] = gc(content)
        content = ''
        info = line[1:].strip()
    else:
        content += line.strip()
gc_strands[info] = gc(content)

for x, y in sorted(gc_strands.items()):
    print(x + " : " + str(y))
