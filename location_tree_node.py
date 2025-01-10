import random
from internal import support as vpt_support

class LocationTreeNode:

    # points is a collection of SearchablePoint
    # distance_calc_function is a function that takes two SearchablePoint(s) and returns the distance between them
    # capacity is the maximum number of nodes to store in this node
    def __init__(self, points, distance_calc_function, capacity = 32):
        self.points = points
        self.distanceCalcFunction = distance_calc_function
        self.capacity = capacity
        self.threshold = 0.0
        self.closer = None
        self.farther = None
        self._protected_initialize_node()

    def _protected_initialize_node(self):
        if len(self.points) == 0:
            if self.closer.size() == 0 or self.farther.size() == 0:
                # Prune empty child nodes.
                self.add_all_points_to_collection(self.points)
                self.closer = None
                self.farther = None
                self._protected_initialize_node()
            else:
                if self.closer is not None:
                    self.closer._protected_initialize_node()
                if self.farther is not None:
                    self.farther._protected_initialize_node()
        else:
            # What matters is that the points within the distance threshold of the
            # vantage point are on the left of the vantage point index in the list
            # and the others are on the right.
            self.vantage_point = random.choice(self.points)
            distance_clac_lambda = vpt_support.get_distance_function_lambda(self.distanceCalcFunction, self.vantage_point)
            self.points = sorted(self.points, key=distance_clac_lambda)
            if len(self.points) > self.capacity :
                self.threshold = self.distanceCalcFunction(self.vantage_point, self.points[ int(len(self.points) / 2) ])
                first_past_threshold = vpt_support.get_index_first_past_threshold(self.distanceCalcFunction, self.vantage_point, self.points, self.threshold)
                if first_past_threshold is None:
                    self.closer = None
                    self.farther = None
                else:
                    cutoff = min(self.capacity, first_past_threshold)
                    points_to_keep = self.points[:cutoff]
                    if first_past_threshold > cutoff:
                        self.closer = LocationTreeNode(self.points[cutoff:first_past_threshold], self.distanceCalcFunction, self.capacity)
                    self.farther = LocationTreeNode(self.points[first_past_threshold:], self.distanceCalcFunction, self.capacity)
                    self.points = points_to_keep

    def size(self):
        closer_size = 0 if self.closer is None else len(self.closer.points)
        farther_size = 0 if self.farther is None else len(self.farther.points)
        return closer_size + farther_size if len(self.points) == 0 else len(self.points)

    def add_all_points_to_collection(self, collection):
        if len(self.points) == 0:
            if self.closer is not None:
                self.closer.add_all_points_to_collection(collection)
            if self.farther is not None:
                self.farther.add_all_points_to_collection(collection)
        else:
            for point in self.points:
                collection.append(point)

    def get_child_node_for_point(self, searchable_point):
        if self.distanceCalcFunction(self.vantage_point, searchable_point) <= self.threshold:
            return self.closer
        else:
            return self.farther

    def add_point(self, searchable_point):
        if len(self.points) == 0:
            self.get_child_node_for_point(searchable_point)
        else:
            self.points.append(searchable_point)

    def remove_point(self, searchable_point):
        if len(self.points) == 0:
            node = self.distanceCalcFunction(self.vantage_point, searchable_point)
            if node is not None:
                node.remove_point(searchable_point)
        else:
            self.points.remove(searchable_point)