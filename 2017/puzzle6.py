import numpy as np

file = open('puzzle6input', 'r')
input = file.read()
input = input.split('\t')
for i in range(len(input)):
    input[i] = int(input[i])

def used_state(input, loop_size_check = False):
    if loop_size_check == False:
        found = False
        states_memory = []
        cycles = 0
        while not found:
            i = np.argmax(input)
            blocks = input[i]
            input[i] = 0
            state = ''
            
            while blocks != 0:
                i += 1
                input[i%len(input)] += 1
                blocks -= 1
                
            for i in range(len(input)):
                state += str(input[i])
                
            if state in states_memory:
                found = True
            else:
                states_memory.append(state)

            cycles += 1

        return cycles, input
    else:
        state = ''
        loop_size = 0
        initial_state = ''
        for i in range(len(input)):
            initial_state += str(input[i])
        while state != initial_state:
            i = np.argmax(input)
            blocks = input[i]
            input[i] = 0
            state = ''
            
            while blocks != 0:
                i += 1
                input[i%len(input)] += 1
                blocks -= 1
                
            for i in range(len(input)):
                state += str(input[i])

            loop_size += 1

        return loop_size

    

cycles, new_input = used_state(input)

loop_size = used_state(new_input, loop_size_check=True)

print(loop_size)


