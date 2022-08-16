import math
import common_lib

def classify(point, dataframe):

    dists = []
    for arr in dataframe:
        cat = arr[len(arr) - 1]
        dist = 0
        for i in range(len(arr) - 1):
            try:
                a = float(arr[i])
                b = float(point[i])
                dist += ((a - b) ** 2)
            except:
                continue
            dist = math.sqrt(dist)
            dists.append([dist, cat])
    
    # k = round(0.1 * len(dataframe))
    # if (k > 30):
    #     k = 30

    k = 5

    dists.sort(key=lambda x: x[0])
    freqs = {}
    for i in range(0, k):
        cat = dists[i][1]
        if cat in freqs:
            freqs[cat] += 1
        if cat not in freqs:
            freqs[cat] = 1
    
    max = 0
    max_cat = ''
    for cat in freqs:
        if freqs[cat] > max:
            max = freqs[cat]
            max_cat = cat

    return max_cat

dataframe = common_lib.dataframe('dataset_numerical_small.csv')
total = 0
correct = 0
for point in dataframe:
    real = point[len(point) - 1]
    predicted = classify(point, dataframe)
    total += 1
    if predicted == real:
        correct += 1
print('accuracy: ' + str(correct / total))