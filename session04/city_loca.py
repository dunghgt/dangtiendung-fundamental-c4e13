from haversine import haversine

hanoi = {
    'name': 'Ha Noi',
    'lat': 21,
    'lng': 105
}
danang = {
    'name': 'Da Nang',
    'lat': 16,
    'lng': 108
}

saigon = {
    'name': 'Sai Gon',
    'lat': 10.8,
    'lng': 106.6
}

paris = {
    'name': 'paris',
    'lat': 48.8,
    'lng': 2.4
}
ls_city = [hanoi, danang, saigon, paris]

# for (i, j) in enumerate(list_city):
    # list_city[i] = (j['lat'], j['lng'])

for i in range(len(ls_city) - 1):

    for j in range(i + 1, len(ls_city)):

        city1 = ls_city[i]
        city2 = ls_city[j]

        cord1 = (city1['lat'], city1['lng'])
        cord2 = (city2['lat'], city2['lng'])

        distance = haversine(cord1, cord2)
        print("Khoang cach tu {0} den {1} la {2}".format(city1['name'], city2['name'], distance))
