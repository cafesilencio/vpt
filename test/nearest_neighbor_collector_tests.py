import unittest
import location_point as lp
from internal.nearest_neighbor_collector import NearestNeighborCollector
from internal import support as support

class NearestNeighborCollectorTests(unittest.TestCase):

    def test_offer_point(self):
        p0 = lp.SearchablePoint(48.4063228, -122.6915171)
        p1 = lp.SearchablePoint(47.6319725, -122.3487409)
        p2 = lp.SearchablePoint(47.6037785, -122.3418052)
        p3 = lp.SearchablePoint(47.67486628058979, -122.37279870431401)
        origin_point = lp.SearchablePoint(47.6756757, -122.3949482)
        collector = NearestNeighborCollector(support.distance_calc_haversine, origin_point, 3)
        collector.offer_point(p0)
        collector.offer_point(p1)
        collector.offer_point(p2)
        collector.offer_point(p3)
        self.assertEqual(p2, collector.get_farthest_point())

    def test_collected_neighbors(self):
        p0 = lp.SearchablePoint(48.4063228, -122.6915171)
        p1 = lp.SearchablePoint(47.6319725, -122.3487409)
        p2 = lp.SearchablePoint(47.6037785, -122.3418052)
        p3 = lp.SearchablePoint(47.67486628058979, -122.37279870431401)
        origin_point = lp.SearchablePoint(47.6756757, -122.3949482)
        collector = NearestNeighborCollector(support.distance_calc_haversine, origin_point, 3)
        collector.offer_point(p0)
        collector.offer_point(p1)
        collector.offer_point(p2)
        collector.offer_point(p3)
        collected = collector.get_all_collected()
        self.assertEqual(3, len(collected))
        self.assertEqual(p3, collected[0])
        self.assertEqual(p1, collected[1])
        self.assertEqual(p2, collected[2])