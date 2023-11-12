convertion_dict={
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'
}
cDS = "ctagagtccgcaaaaatcaccagtctctctctacaaatctatctctctctatttttctccagaataatgtgtgagtagttcccagataagggaattagggttcttatagggtttcgctcatgtgttgagcatataagaaacccttagtatgtatttgtatttgtaaaatacttctatcaataaaatttctaattcctaaaaccaaaatccagtgacc"
F_adapter = "GGGGCCAACTTTCTTGTACAAAGTGG"
R_adapter = "GGGGACAACTTTGTATAATAAAGTTGGC"
start = cDS[0:20].upper()
compl_seq = ""
for letter in cDS[-1:-21:-1]:
    compl_seq = compl_seq + convertion_dict[letter.upper()]
F_primer = F_adapter + start
R_primer = R_adapter + compl_seq
print(F_primer, R_primer )