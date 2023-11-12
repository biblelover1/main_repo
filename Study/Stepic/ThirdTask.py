red_fragment = "TAAACGTCGAACAGTCATGAAAGTCTTAGTACCAGACATACCATTTTACTGTGAATATTATTTGAAGCTG"
blue_fragment = "ATTTCTTCAAACATTTAAAAATAAAGACTTATTGTAGACAGAGGTACGCCCTTTTAATGGTTGCGATAAA"

p1 = red_fragment[-20::] + blue_fragment[0:20]

def Compr(seq):
    dict1 = {"A": "T",
         "T": "A",
         "C": "G",
         "G":"C"}
    compr = ""
    for letter in seq:
        compr += dict1[letter]
    return compr
p2 = Compr(p1[-1::-1])
# print(p1, p2)

def Rev_trans(seq):
    dict1 = {"A": "T",
         "U": "A",
         "C": "G",
         "G":"C"}
    compr = ""
    for letter in seq:
        compr += dict1[letter]
    return compr

mRNK = "UAUGCAUGCAUGCAUCGACGAUCUGCAGACGAAAAAAAAAAAAAAAAAAAAAAAAA"
cDNK = Rev_trans(mRNK)
print(cDNK[-1::-1])















