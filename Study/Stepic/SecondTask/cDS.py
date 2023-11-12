convertion_dict={
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'
}
cDS = "ATGGACAAATGCAAAAAAGTGTACGAAAACTACCCGGTGTCCAAATGCCAGCTGGCGAACCAGTGCAACTACGACTGCAAACTGGACAAACACGCGCGCTCCGGCGAATGCTTCTACGACGAAAAACGCAACCTGCAGTGCATCTGCGACTACTGCGAATACTAA"
F_adapter = "GGGGACAACTTTGTACAAAAAAGTTGGC"
R_adapter = "GGGGACAACTTTGTACAAGAAAGTTGG"
start = cDS[0:20]
compl_seq = ""
for letter in cDS[-1:-21:-1]:
    compl_seq = compl_seq + convertion_dict[letter.upper()]
F_primer = F_adapter + start
R_primer = R_adapter + compl_seq
print(F_primer, R_primer )