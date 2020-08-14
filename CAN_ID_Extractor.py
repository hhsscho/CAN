f = open("D:\\can_data\\2020-08-12_16-59-55_EQ900_Idle.asc", "r")
output = open("D:\\eq900_id_list.txt", "w")
lines = f.readlines()

ID = []
for line in lines[4:]:
    id = line[15:18]
    if id not in ID:
        ID.append(id)

for id in ID:
    output.write(id)
    output.write("\n")
print(len(ID))