convertion_dict={
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'
}

start = "ggaggtattccaatcccacaaaaatctgagcttaacagcacagt"
start = start[0:20]
F_adapt = "GGGGACAACTTTGTATAGAAAAGTTGGC"
R_adapt = "GGGGCCAACTTTTTTGTACAAAGTTG"
end = "ttacaattacatttacaattatcgataca"
end = end[-1:-21:-1]
print(end)
seq = ""
for letter in end:
    seq = seq + convertion_dict[letter.upper()]
print(seq)
F_primer = F_adapt + start.upper()
R_primer = R_adapt + seq
print(F_primer, R_primer)