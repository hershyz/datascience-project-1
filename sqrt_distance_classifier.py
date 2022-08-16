import math
import common_lib

def classify(point, model):

    dists = {}

    for cat in model:
        arr = model[cat]
        cat_dist = 0
        for i in range(len(arr)):
            try:
                cat_dist += (arr[i] - float(point[i])) ** 2
            except:
                continue
        dists[cat] = math.sqrt(cat_dist)
    
    min = 10000000000
    min_cat = ''
    for cat in dists:
        if dists[cat] < min:
            min_cat = cat
            min = dists[cat]
    
    return min_cat

# dataframe = common_lib.dataframe('dataset_numerical.csv')
dataframe = common_lib.dataframe('strokes.csv')
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