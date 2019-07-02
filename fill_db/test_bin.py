import psycopg2
from argparse import ArgumentParser


def byTime_key(point):
    return point['time']


if __name__ == '__main__':

    parser = ArgumentParser()

    parser.add_argument(
        '-f', '--filepath', type=str,
        required=True, help="Set file's path"
    )
    arg = parser.parse_args()
    file_path = arg.filepath
    with open(file_path, 'rb') as file:
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
    if not start_id[0]:
        start_id = 0
    conn.commit()

    # Заполняем базу точками
    s = "INSERT INTO mainapp_point(time, val, more_time, less_time, more_value, less_value) VALUES"
    for _ in range(len(data_points)):
        s = s + ' (%s, %s, %s, %s, %s, %s),'
    s = s[:-1]
    points = list()
    for point_elem in data_points:
        points += point_elem['time'], \
                  point_elem['value'], \
                  point_elem['more_time'], \
                  point_elem['less_time'], \
                  point_elem['more_value'],\
                  point_elem['less_value']
    cur.execute(s, points)
    conn.commit()

    # Получаем точки, которые записали, но уже с ID
    cur.execute("SELECT * FROM mainapp_point WHERE id > %s", (start_id,))
    info = cur.fetchall()
    conn.commit()

    intervals = list()
    for i in range(len(info) - 1):
        for j in range(i+1, len(info)):
            intervals += info[j][1] - info[i][1], info[i][0], info[j][0]

    s = "INSERT INTO mainapp_interval(val, point_a_id, point_b_id) VALUES"
    for _ in range(len(intervals) // 3):
        s = s + ' (%s, %s, %s),'
    s = s[:-1]

    # Записываем интервалы в БД
    cur.execute(s, intervals)
    conn.commit()
    print('All points and intervals uploaded to database')
    choice = input('Вы хотите создать комментарий? (y/n): ')
    if choice == 'y':
        start_interval = int(input('Введите интервал с: '))
        finish_interval = int(input('до: '))
        text = input('Теперь введите Ваш комментарий: ')
        cur.execute(
            "INSERT INTO mainapp_comment(text, start_time, finish_time) "
            "VALUES (%s, %s, %s)",
            (text, start_interval, finish_interval)
        )
        conn.commit()
        print('Your comment uploaded to database')
    else:
        print('Bye-bye! =)')
    cur.close()
    conn.close()
