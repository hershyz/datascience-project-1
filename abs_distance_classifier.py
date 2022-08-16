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

dataframe = common_lib.dataframe('dataset_numerical.csv')
model = common_lib.common_model('dataset_numerical.csv')

total = 0
correct = 0
for point in dataframe:
    real = point[len(point) - 1]
    predicted = classify(point, model)
    total += 1
    if predicted == real:
        correct += 1
print('accuracy: ' + str(correct / total))