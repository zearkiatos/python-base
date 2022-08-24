def interspersed_strings(string1: str, string2: str) -> str:
    list1 = string1.split()
    list2 = string2.split()
    new_list = ''
    print(list1,list2)

    for i in range(0, len(list1)):
        for j in range(i, i+1):
            new_list += " "+list1[i]+" "+list2[j]

    return new_list


string1 = 'La casa está cerca río'
string2 = 'linda no muy del grande'

print(interspersed_strings(string1, string2))
