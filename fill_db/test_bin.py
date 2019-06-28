from random import randint


def byTime_key(point):
    return point['time']


with open('file.bin', 'rb') as file:
    header = file.read(20).decode('utf-8')
    more_time, less_time, more_value, less_value = [x for x in file.read(4)]
    lst_values = [x for x in file.read()]
    data_points = list()
    for i in range(0, len(lst_values), 2):
        point = dict()

        point['time'] = lst_values[i]
        point['value'] = lst_values[i + 1]
        point['more_time'] = more_time
        point['less_time'] = less_time
        point['more_value'] = more_value
        point['less_value'] = less_value
        data_points.append(point)

# Сортируем по времени
data_points = sorted(data_points, key=byTime_key)
intervals = list()

for c in data_points:
    print(c)

for i in range(len(data_points) - 1):
    for j in range(i+1, len(data_points)):
        interval = dict()
        interval['val'] = data_points[j]['time'] - data_points[i]['time']
        interval['point_a'] = data_points[i]
        interval['point_b'] = data_points[j]
        intervals.append(interval)

# print(len(intervals))
#
# [print(intervals[randint(0, 4949)]) for _ in range(5)]

# for c in intervals:
#     print(c)