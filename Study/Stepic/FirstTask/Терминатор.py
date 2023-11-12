f_adapter = "GTAGGTCTCAGTAA"
s_adapter = "GTAGGTCTCTAAGG"
start = "ccaggcatcaaataaaacga"
end = "accttcgggtgggcctttctgcgtttata"
end = end[len(end):-21:-1]
end_list = []
end_list.append(end)



# def reversed1(variable):
#     res=''
#     for i in range(len(variable)-1,-1,-1):
#         res+=variable[i]
#     return res

# end_rev = reversed1(end)

def compliment_chain(chain):
    compl = ""
    for i in chain:
        if i == "a":
            compl += 't'
        elif i == 't':
            compl += 'a'
        elif i == 'g': 
            compl += 'c'
        elif i == 'c':
             compl += 'g' 
    return compl

new_chain = compliment_chain(end)
f_primer = f_adapter + start.upper()
r_primer = s_adapter + new_chain.upper()
print(f_primer, r_primer)
print(len(f_primer), len(r_primer))


