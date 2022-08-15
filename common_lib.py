# taken from SCE boilerplate code

from copy import deepcopy

def dataframe(csv_path):
    f = open(csv_path, 'r')
    point_arr = []
    lines = f.readlines()
    for i in range(1, len(lines)):
        line = lines[i]
        line = line.replace('\n', '')
        point_arr.append(line.split(','))
    return point_arr