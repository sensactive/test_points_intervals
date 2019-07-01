from random import randint
import psycopg2


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

conn = psycopg2.connect(dbname='django_db', user='admin', password='admin', host='localhost', port=5432)
cur = conn.cursor()
# Получаем последний индекс в БД
cur.execute("SELECT MAX(id) FROM mainapp_point")
start_id = cur.fetchone()
conn.commit()
# TODO Сделать один запрос, а не циклические
for point_elem in data_points:
    cur.execute("INSERT INTO mainapp_point("
                "time,"
                " val,"
                " more_time,"
                " less_time,"
                " more_value, "
                "less_value"
                ") VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    point_elem['time'],
                    point_elem['value'],
                    point_elem['more_time'],
                    point_elem['less_time'],
                    point_elem['more_value'],
                    point_elem['less_value']
                )
                )

conn.commit()
# Получаем точки, которые записали, но уже с ID
cur.execute("SELECT * FROM mainapp_point WHERE id > %s", (start_id,))
info = cur.fetchall()

conn.commit()

intervals = list()

for i in range(len(info) - 1):
    for j in range(i+1, len(info)):

        intervals.append(info[j][1] - info[i][1])
        intervals.append(info[i][0])
        intervals.append(info[j][0])

# Формируем строку для одного запроса к БД на запись всех интервалов
s = "INSERT INTO mainapp_interval(val, point_a_id, point_b_id) VALUES"
for _ in range(len(intervals) // 3):
    s = s + ' (%s, %s, %s),'
s = s[:-1]

# Записываем интервалы в БД
cur.execute(s, intervals)
conn.commit()

cur.close()
conn.close()


