file = open('puzzle8input','r')
line = file.readline().rstrip().split()

reg_dict = {}
largest = 0

while line != []:
    reg_to_mod = line[0]
    mod = line[1]
    mod_by = int(line[2])
    reg_check = line[4]
    condition = line[5]
    cond_value = int(line[6])
    
    if reg_to_mod not in reg_dict:
        reg_dict[reg_to_mod] = 0
    if reg_check not in reg_dict:
        reg_dict[reg_check] = 0

    if condition == '>' and reg_dict[reg_check] > cond_value:
        if mod == 'inc':
            reg_dict[reg_to_mod] += mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
        else:
            reg_dict[reg_to_mod] -= mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
    elif condition == '<' and reg_dict[reg_check] < cond_value:
        if mod == 'inc':
            reg_dict[reg_to_mod] += mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
        else:
            reg_dict[reg_to_mod] -= mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
    elif condition == '>=' and reg_dict[reg_check] >= cond_value:
        if mod == 'inc':
            reg_dict[reg_to_mod] += mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
        else:
            reg_dict[reg_to_mod] -= mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
    elif condition == '<=' and reg_dict[reg_check] <= cond_value:
        if mod == 'inc':
            reg_dict[reg_to_mod] += mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
        else:
            reg_dict[reg_to_mod] -= mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
    elif condition == '==' and reg_dict[reg_check] == cond_value:
        if mod == 'inc':
            reg_dict[reg_to_mod] += mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
        else:
            reg_dict[reg_to_mod] -= mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
    elif condition == '!=' and reg_dict[reg_check] != cond_value:
        if mod == 'inc':
            reg_dict[reg_to_mod] += mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
        else:
            reg_dict[reg_to_mod] -= mod_by
            if reg_dict[reg_to_mod] > largest:
                largest = reg_dict.get(reg_to_mod)
            line = file.readline().rstrip().split()
    else:
        line = file.readline().rstrip().split()

print(largest)
