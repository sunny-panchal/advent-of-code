from collections import Counter

def openfile(x=2):
    if x == 1:
        file=open('puzzle7input','r')
    elif x == 2:
        file=open('puzzle7testdata','r')
    return file

def find_root(x=2):
    file = openfile(x)
    data = file.readline().rstrip().split()
    sub_towers = []
    possible_root = []
    root = ''
    
    while data != []:
        if len(data) == 2:
            sub_towers.append(data[0])
        else:
            possible_root.append(data[0])
            i = 3
            while i != len(data):
                sub_towers.append(data[i].rstrip(','))
                i += 1
        data = file.readline().rstrip().split()

    for word in possible_root:
        if word not in sub_towers:
            root += word

    return root


def make_values_dict(x=2):
    file = openfile(x)
    data = file.readline().rstrip().split()
    values = {}
    while data != []:
        if data[0] not in values:
            values[data[0]] = int(data[1].lstrip('(').rstrip(')'))
        data = file.readline().rstrip().split()
    return values

def make_dict(x=2):
    file = openfile(x)
    data = file.readline().rstrip().split()
    proc_data = []
    data_dict={}
    while data != []:
        proc_data.append(data)
        data = file.readline().rstrip().split()

    for data in proc_data:
        if len(data) > 2:
            i = 3
            data_dict[data[0]]=[]
            while i != len(data):
                data_dict[data[0]].append(data[i].rstrip(','))
                i += 1
    return data_dict

x = int(input('Enter 1 for input data, 2 for test: '))    
value_dict = make_values_dict(x)
data_dict = make_dict(x)
check = find_root(x)
   
def find_imbalance(x=2, value_dict=value_dict, data_dict=data_dict, check=check):
    root_value = []
    root_names = []
    temp = data_dict.get(check)
    for name in temp:
        root_names.append([name])
    for i in range(len(data_dict[check])):
        root_value.append([value_dict[root_names[i][0]]])
    for i in range(len(root_value)):
        check = root_names[i][0]
        # All values in data_dict are holding up other names
        while check in data_dict:
            temp = data_dict.get(check)
            for name in temp:
                root_names[i].append(name)
            j=0
            while j != len(root_names[i]):
                for j in range(1,len(root_names[i])):
                    check = root_names[i][j]
                    temp = data_dict.get(check)
                    if temp != None:
                        for name in temp:
                            if name not in root_names[i]:
                                root_names[i].append(name)
                    j += 1

    for i in range(len(root_value)):
        for j in range(1,len(root_names[i])):
            root_value[i][0] += value_dict[root_names[i][j]]

    cnt = Counter()
    temp = root_value
    root_value = []
    for value in temp:
        root_value.append(value[0])
    for value in root_value:
        cnt[value] += 1

    if len(cnt) == 2:
        y = cnt.most_common(1)
        y = y[0][0]
        i = 0
        while y == root_value[i]:
           i+= 1
        imbalance = root_names[i][0]
        diff = root_value[i] - y
    else:
        imbalance = 'balanced'
        diff = 0

##    print(imbalance)                
            
    return root_value, root_names, imbalance, diff

def imbalanced_number(x=2, value_dict=value_dict, data_dict=data_dict, check=check):
    found = False
    imbalance = check
    base = []
    while not found:
        root_value, root_names, check, diff = find_imbalance(check=imbalance)
        if check == 'balanced':
            found = True
        else:
            base.append(imbalance)
            imbalance = check
##    index = data_dict[base[-1]].index(imbalance)
    if base != []:
        _, _, _, diff = find_imbalance(base[-1])
        number = value_dict[imbalance]
        number -= diff
    else:
        imbalance = check
        number = 'Everything looks good'
    
    return imbalance, number


    
    
