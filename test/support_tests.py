import functools
import unittest

from internal import support as support
import location_point as lp

class SupportTests(unittest.TestCase):

    def testHaversineDistance(self):
        p1 = lp.SearchablePoint(47.6319725,-122.3487409)
        p2 = lp.SearchablePoint(47.6037785,-122.3418052)
        result = support.distance_calc_haversine(p1, p2)
        self.assertEqual(3177.843269595496, result)

    def testGetDistanceFunctionLambda(self):
        p0 = lp.SearchablePoint(48.4063228, -122.6915171)
        p1 = lp.SearchablePoint(47.6319725,-122.3487409)
        p2 = lp.SearchablePoint(47.6037785,-122.3418052)
        points = [p0, p1, p2]
        vantage_point = lp.SearchablePoint(47.6756757, -122.3949482)
        distance_lambda = support.get_distance_function_lambda(support.distance_calc_haversine, vantage_point)
        results = sorted(points, key=distance_lambda)
        self.assertEqual(results[0], p1)
        self.assertEqual(results[1], p2)
        self.assertEqual(results[2], p0)

    def testGetIndexOfFirstPastThreshold(self):
        p0 = lp.SearchablePoint(48.4063228, -122.6915171)
        p1 = lp.SearchablePoint(47.6319725,-122.3487409)
        p2 = lp.SearchablePoint(47.6037785,-122.3418052)
        p3 = lp.SearchablePoint(47.104326,-122.4302807)
        vantage_point = lp.SearchablePoint(47.6756757, -122.3949482)
        distance_lambda = support.get_distance_function_lambda(support.distance_calc_haversine, vantage_point)
        points = sorted([p0, p1, p2, p3], key=distance_lambda)
        threshold = support.distance_calc_haversine(vantage_point, p2)
        index = support.get_index_first_past_threshold(support.distance_calc_haversine, vantage_point, points, threshold)
        self.assertEqual(2, index)

    def testGetLocationComparator(self):
        p0 = lp.SearchablePoint(48.4063228, -122.6915171)
        p1 = lp.SearchablePoint(47.6319725, -122.3487409)
        p2 = lp.SearchablePoint(47.6037785, -122.3418052)
        p3 = lp.SearchablePoint(47.67486628058979, -122.37279870431401)
        origin_point = lp.SearchablePoint(47.6756757, -122.3949482)
        comparator = support.get_location_comparator(origin_point, support.distance_calc_haversine)
        points = sorted([p0, p1, p2, p3], key=functools.cmp_to_key(comparator))
        self.assertEqual(p3, points[0])