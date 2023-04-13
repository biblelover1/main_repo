# Напишите программу для печати всех уникальных значений в словаре.

a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {"VIII" : "S007"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
res = []
for i in a:
    print(f"{i}n/")
    for val in i.values():
        if val not in res:
            res.append(val)
print(res)