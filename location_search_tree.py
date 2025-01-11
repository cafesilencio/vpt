from internal.nearest_neighbor_collector import NearestNeighborCollector
from internal.support import distance_calc_haversine
from location_tree_node import LocationTreeNode

class LocationSearchTree:

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.root_node = None
        self.distance_calc_function = distance_calc_haversine #todo make this variable so support different strategies

    def add_location_points(self, location_points):
        if self.root_node is None:
            self.root_node = LocationTreeNode(location_points, self.distance_calc_function, self.capacity)
        else:
            if len(location_points) > 0:
                for point in location_points:
                    self.root_node.add_point(point)
                self.root_node.protected_initialize_node()

    def clear(self):
        self.root_node = None

    def get_nearest_neighbor(self, target_point):
        return self.get_nearest_neighbors(target_point, 1)

    def get_nearest_neighbors(self, target_point, max_results = 1):
        if self.root_node is not None:
            collector = NearestNeighborCollector(self.distance_calc_function, target_point, max_results)
            self.root_node.collect_nearest_neighbors(collector)
            results = collector.get_all_collected()
            cutoff = min(max_results, len(results))
            return results[0:cutoff]
        else:
            return []