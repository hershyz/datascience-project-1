import math
import common_lib

def classify(point, model):

    distances = {}
    for cat in model:
        cat_distance = 0
        cat_arr = model[cat]
        for i in range(0, len(cat_arr)):
            try:
                cat_distance += abs(cat_arr[i] - float(point[i]))
            except:
                continue
        distances[cat] = cat_distance
    
    min_distance = 1000000000000
    min_cat = ''
    for cat in distances:
        if distances[cat] < min_distance:
            min_distance = distances[cat]
            min_cat = cat

    return min_cat






dataframe = common_lib.dataframe('features_removed.csv')
model = common_lib.common_model('features_removed.csv')

f = open('features_removed.csv', 'r')
raw = f.readlines()
feature_labels = raw[0].replace('\n', '')

fnew = open('features_removed.csv', 'w')
fnew.write(feature_labels)

for point in dataframe:
    predicted = classify(point, model)
    point.append(predicted)
    point_string = str(point)
    point_string = point_string.replace('[', '')
    point_string = point_string.replace(']', '')
    point_string = point_string.replace('\'', '')
    point_string = point_string.replace(' ', '')
    fnew.write(point_string + '\n')