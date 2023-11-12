# Область сDS
seq = "aatacaactccctcacagcgattaggttttttgcat"
end_seq = "aacgcgggcgcagggcacgacaaaagaagg"
seq = seq[0:20]
start = "GTAGGTCTCATATG"
end = "GTAGGTCTCTTTAC"
end_seq_rev = end_seq[len(end_seq):-21:-1]
end_seq_rev_list = []
for i in end_seq_rev:
    end_seq_rev_list.append(i)
for i in range(0, len(end_seq_rev_list)):
    if end_seq_rev_list[i] == 'a':
        end_seq_rev_list[i] = 't'
    elif end_seq_rev_list[i] == 't':
        end_seq_rev_list[i] = 'a'
    elif end_seq_rev_list[i] == 'g':
        end_seq_rev_list[i] = 'c'
    elif end_seq_rev_list[i] == 'c':
        end_seq_rev_list[i] = 'g'
new_seq = "".join(end_seq_rev_list)
print(start+seq.upper(), end+new_seq.upper())

