import numpy as np

def side_length(layer):
    side_length = 2 * layer
    return side_length

def number_of_elements(layer):
    number_of_elements = (8 * (layer-1)) + 4
    return number_of_elements
input = 265149
def top_left(layer):
    top_left = 0
    for i in range(layer):
        top_left += number_of_elements(i+1)
    return top_left

def top_right(layer):
    top_right = top_left(layer) - side_length(layer) + 1
    return top_right

def bottom_right(layer):
    bottom_right = top_right(layer) - side_length(layer) + 1
    return bottom_right

def bottom_left(layer):
    bottom_left = bottom_right(layer) - side_length(layer) + 1
    return bottom_left

def which_layer(input):
    top_left_number = 0
    layer = 0
    while top_left_number < input:
        layer += 1
        top_left_number = top_left(layer)
    return layer

def which_side(input):
    layer = which_layer(input)
    side_len = side_length(layer)
    side = ''
    if input < bottom_left(layer):
        side = 'left'
    elif input < bottom_right(layer):
        side = 'bottom'
    elif input < top_right(layer):
        side = 'right'
    elif input < top_left(layer):
        side = 'top'
    return side

def closest_side(input):
    side = which_side(input)
    layer = which_layer(input)
    bl = bottom_left(layer)
    br = bottom_right(layer)
    tl = top_left(layer)
    tr = top_right(layer)
    closest = 'corner'

    if side == 'bottom':
        if (input - bl) > (br - input):
            closest = 'right'
        else:
            closest = 'left'
    elif side == 'top':
        if (input - tr) > (tl - input):
            closest = 'left'
        else:
            closest = 'right'
    elif side == 'right':
        if (input - br) > (tr - input):
            closest = 'top'
        else:
            closest = 'bottom'
    elif side == 'left':
        if (bl - input) >= (side_length(layer)/2):
            closest = 'top'
        else:
            closest = 'bottom'
    return closest

def below(layer):
    br = bottom_right(layer)
    half_length = side_length(layer)/2
    below = br - half_length
    return below

def hor_spaces(input):
    hor_spaces = input - below(which_layer(input))
    return hor_spaces

def ver_spaces(input):
    ver_spaces = which_layer(input) - 1
    return ver_spaces

def total_steps(input):
    return ver_spaces(input) + hor_spaces(input)

spiral = [0, 1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54, 57, 59, 122, 133, 142]
i = 17
while spiral[i-1] <= 265149:
    ## start a loop from 5 onwards to fill in all the values of the array
    ## while filling, run a condition to check side and corner
    ## if corner condition is met, add rules, else add rule based on side
    layer = which_layer(i)
    prev_1layer = layer - 1
    prev_2layer = layer - 2
    tlpl1 = top_left(prev_1layer)
    tlpl2 = top_left(prev_2layer)
    blpl1 = bottom_left(layer - 1)
    blpl2 = bottom_left(layer - 2)
    brpl1 = bottom_right(layer-1)
    brpl2 = bottom_right(layer-2)
    trpl1 = top_right(layer-1)
    trpl2 = top_right(layer-2)
    ## first block in new layer
    if (i - tlpl1) == 1:
        spiral.append(spiral[tlpl1] + spiral[tlpl2+1])
    ## before bottom left corner block
    elif (bottom_left(layer) - i) == 1:
        spiral.append(spiral[i-1] + spiral[blpl1] + spiral[blpl1-1])
    ## bottom left corner block
    elif i == bottom_left(layer):
        spiral.append(spiral[i-1] + spiral[blpl1])
    ## just after bottom left corner block
    elif (i - 1) == bottom_left(layer):
        spiral.append(spiral[i-1] + spiral[i-2] + spiral[blpl1] + spiral[blpl1+1])
    ## just before bottom right
    elif (i + 1) == bottom_right(layer):
        spiral.append(spiral[i-1] + spiral[brpl1] + spiral[brpl1-1])
    ## bottom right
    elif i == bottom_right(layer):
        spiral.append(spiral[i-1] + spiral[brpl1])
    ## just after bottom right
    elif (i - 1) == bottom_right(layer):
        spiral.append(spiral[i-1] + spiral[i-2] + spiral[brpl1] + spiral[brpl1+1])
    ## just before top right
    elif (i + 1) == top_right(layer):
        spiral.append(spiral[i-1] + spiral[trpl1] + spiral[trpl1-1])
    ## top right
    elif i == top_right(layer):
        spiral.append(spiral[i-1] + spiral[trpl1])
    ## just after top right
    elif (i - 1) == top_right(layer):
        spiral.append(spiral[i-1] + spiral[i-2] + spiral[trpl1] + spiral[trpl1+1])
    ## just before top left
    elif (i + 1) == top_left(layer):
        spiral.append(spiral[i-1] + spiral[tlpl1] + spiral[tlpl1-1] + spiral[tlpl1+1])
    ## top left
    elif i == top_left(layer):
        spiral.append(spiral[i-1] + spiral[tlpl1] + spiral[tlpl1+1])
    ## all other cases on left
    elif which_side(i) == 'left':
        index = i - tlpl1
        if i == (tlpl1 + 2):
            spiral.append(spiral[i-1] + spiral[i-2] + spiral[tlpl2+1] + spiral[tlpl2+2])
        else:
            spiral.append(spiral[i-1] + spiral[tlpl2+index-1] + spiral[tlpl2+index-2] + spiral[tlpl2+index])
    ## all other cases on bottom
    elif which_side(i) == 'bottom':
        index = i - bottom_left(layer)
        spiral.append(spiral[i-1] + spiral[blpl1+index-2] + spiral[blpl1+index-1] + spiral[blpl1+index])
    ## all other cases on right
    elif which_side(i) == 'right':
        index = i - bottom_right(layer)
        spiral.append(spiral[i-1] + spiral[brpl1+index-2] + spiral[brpl1+index-1] + spiral[brpl1+index])
    ## all other cases on top
    elif which_side(i) == 'top':
        index = i - top_right(layer)
        spiral.append(spiral[i-1] + spiral[trpl1+index-2] + spiral[trpl1+index-1] + spiral[trpl1+index])
    i += 1
