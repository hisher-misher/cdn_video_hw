import pandas as pd
import math

cities_df = pd.read_csv('worldcities.csv')

def get_2_clothest_cities(cities, point):
    DIST, CITY = 0, 1
    def get_bigger_distance_ind(clothest):
        """ Возвращает индекс города с большим расстоянием"""
        first = clothest[0]
        second = clothest[1]
        if first[DIST] > second[DIST]:
            return 0
        return 1

    clothest = []
    try:
        x, y = point
        for city in cities:
            dist = math.hypot(x - city.x_coord, y - city.y_coord)
            print(f"dist={dist}")

            # добавляем в список городов котреж (расстояние, город) или заменяем один элемент с большим расстоянием
            if len(clothest) < 2:
                clothest.append((dist, city))
                # print(f"clothest = {clothest}")
                continue
            else:
                bigger_dist_ind = get_bigger_distance_ind(clothest)
                if dist < clothest[bigger_dist_ind][DIST]:
                    clothest[bigger_dist_ind] = (dist, city)
            # print(f"clothest = {clothest}")

    except ValueError:
        return [None, None]
    print(f'point: {x, y}, ')
    city1 = city2 = None
    if len(clothest) >= 1:
        city1 = clothest[0]
    if len(clothest) >= 2:
        city2 = clothest[1]
    return [city1[CITY], city2[CITY]]