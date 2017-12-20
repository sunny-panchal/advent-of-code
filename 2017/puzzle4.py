input = open('puzzle3input','r')

def num_valid1(input):
    passphrase = input.readline()
    total_valid = 0

    while passphrase != '':
        valid = True
        passphrase = passphrase.rstrip()
        passphrase = passphrase.split()
        for word in passphrase:
            if passphrase.count(word) > 1:
                valid = False
        if valid == True:
            total_valid += 1
        passphrase = input.readline()

    return total_valid

def num_valid2(input):
## a = 'ZENOVW'
## ''.join(sorted(a))
## 'ENOVWZ'
    passphrase = input.readline()
    total_valid = 0

    while passphrase != '':
        valid = True
        passphrase = passphrase.rstrip()
        passphrase = passphrase.split()
        processed = []
        for word in passphrase:
            processed.append(''.join(sorted(word)))

        for word in processed:
            if processed.count(word)>1:
                valid = False
        if valid == True:
            total_valid += 1
        passphrase = input.readline()
    return total_valid
