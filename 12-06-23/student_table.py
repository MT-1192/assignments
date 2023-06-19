dict1={1:"Raj", 2:"Sai"}
dict2={1:"90",2:"93"}
print("Roll ","Name ","Marks" )
for k1 in dict1:
    for k2 in dict2:
        if k1 == k2:
            print(k1, "  ", dict1[k1], "  ", dict2[k2])