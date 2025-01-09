from haversine import haversine, Unit

def distance_calc_haversine(location_point1, location_point2):
    p1 = (location_point1.get_latitude(), location_point1.get_longitude())
    p2 = (location_point2.get_latitude(), location_point2.get_longitude())
    return haversine(p1, p2, unit=Unit.METERS)

#def distance_calc_haversine_lambda(location_point):
#    return lambda some_location_point: distance_calc_haversine(location_point, some_location_point)

def get_distance_function_lambda(distance_function, first_point):
    return lambda some_location_point: distance_function(first_point, some_location_point)

def get_index_first_past_threshold(distance_function, vantage_point, points, threshold):
    dist_lambda = lambda point : (point, distance_function(point, vantage_point))
    point_distance_map = map(dist_lambda, points)
    for item in point_distance_map:
        if item[1] > threshold:
            return points.index(item[0])
    return None