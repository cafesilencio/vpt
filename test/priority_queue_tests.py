import unittest
from internal import support as support
from internal.priority_queue import PriorityQueue
import location_point as lp

class PriorityQueueTests(unittest.TestCase):

    def test_queue(self):
        p0 = lp.SearchablePoint(48.4063228, -122.6915171)
        p1 = lp.SearchablePoint(47.6319725, -122.3487409)
        p2 = lp.SearchablePoint(47.6037785, -122.3418052)
        p3 = lp.SearchablePoint(47.67486628058979, -122.37279870431401)
        origin_point = lp.SearchablePoint(47.6756757, -122.3949482)
        comparator = support.get_location_comparator(origin_point, support.distance_calc_haversine)
        queue = PriorityQueue(comparator)
        queue.add(p1)
        queue.add(p0)
        queue.add(p3)
        queue.add(p2)
        self.assertEqual(p0, queue.poll())
        self.assertEqual(3, queue.size())