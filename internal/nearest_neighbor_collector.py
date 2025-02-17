import sys
from internal.priority_queue import PriorityQueue
from internal import support as vpt_support

class NearestNeighborCollector:

    def __init__(self, distance_calc_function, query_point, capacity):
        self.query_point = query_point
        self.capacity = capacity
        self.distance_function = distance_calc_function
        self.distance_comparator = vpt_support.get_location_comparator(query_point, distance_calc_function)
        self.distance_to_farthest_point = 0.0
        self.queue = PriorityQueue(self.distance_comparator)

    def offer_point(self, location_point):
        point_added = False
        if self.queue.size() < self.capacity:
            self.queue.add(location_point)
            point_added = True
        else:
            if self.queue.size() > 0:
                distance_to_new_point = self.distance_function(self.query_point, location_point)
                if distance_to_new_point < self.distance_to_farthest_point:
                    self.queue.poll()
                    self.queue.add(location_point)
                    point_added = True
        #fixme if a point was added won't the queue size always be greater than 0?
        if point_added and self.queue.size() > 0:
            queue_head = self.queue.peek()
            if queue_head is not None:
                self.distance_to_farthest_point = self.distance_function(self.query_point, queue_head)
            else:
                self.distance_to_farthest_point = sys.float_info.max

    def get_farthest_point(self):
        return self.queue.peek()

    # returns all that have been collected sorted by nearest to farthest
    def get_all_collected(self):
        return list(reversed(self.queue.items))
