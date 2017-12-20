file = open('puzzle5input','r')
input = [line.rstrip() for line in file]

def step_function(input):
    old_i = 0
    steps = 0
    while old_i in range(len(input)):
        new_i = old_i + int(input[old_i])
        if int(input[old_i]) >= 3:
            input[old_i] = str(int(input[old_i]) - 1)
        else:
            input[old_i] = str(int(input[old_i]) + 1)
        old_i = new_i
        steps += 1
    return steps
