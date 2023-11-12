mainSeq = "ggttgcttcctataaaaaacttgactctatatctactagaggttttctaatgatggcatccggggaaaaccttgtcaatgaagagcgatc"
mainSeq = mainSeq.upper()
a1 = "GTAGGTCTCAATGC"
a2 = "GTAGGTCTCTCATA"
F_primer = a1 + mainSeq[:20]
reverse = mainSeq[len(mainSeq):-21:-1]
# R_primer = R_adapt + mainSeq[len(mainSeq):-21:-1]
R_primer_list = []
for i in reverse:
    R_primer_list.append(i)

for i in range(0, len(R_primer_list)):
    if R_primer_list[i] == 'A':
        R_primer_list[i] = 'T'
    elif R_primer_list[i] == 'T':
        R_primer_list[i] = 'A'
    elif R_primer_list[i] == 'G':
        R_primer_list[i] = 'C'
    elif R_primer_list[i] == 'C':
        R_primer_list[i] = 'G'
R_primer_list = "".join(R_primer_list)
print(F_primer, a2 + R_primer_list)
