from internal import support as vpt_support

class NearestNeighborCollector:

    def __init__(self, distance_calc_function, query_point, capacity):
        self.query_point = query_point
        self.capacity = capacity
        self.distance_comparator = vpt_support.get_location_comparator(query_point, distance_calc_function)
        self.distance_to_farthest_point = 0.0

    def offer_point(self, location_point):
        pass # fixme remove this