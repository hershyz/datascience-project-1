import common_lib

dataframe = common_lib.dataframe('healthcare-dataset-stroke-data.csv')
f = open('healthcare-dataset-stroke-data.csv', 'w')

for i in range(1, len(dataframe)):
    age = dataframe[i][1]
    stroke = float(dataframe[i][len(dataframe[i]) - 1])
    stroke *= 100
    stroke = str(stroke)
    f.write(age + ', ' + stroke + '\n')