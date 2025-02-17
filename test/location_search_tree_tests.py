import unittest
import location_point as lp
from location_search_tree import LocationSearchTree


class MyTestCase(unittest.TestCase):

    def test_location_tree_collect_nearest_neighbors(self):
        p0 = lp.SearchablePoint(48.4063228, -122.6915171)
        p1 = lp.SearchablePoint(47.6319725, -122.3487409)
        p2 = lp.SearchablePoint(47.6037785, -122.3418052)
        p3 = lp.SearchablePoint(47.67486628058979, -122.37279870431401)
        p4 = lp.SearchablePoint(35.3366116,139.4967988)
        p5 = lp.SearchablePoint(35.9198808,140.121725)
        p6 = lp.SearchablePoint(33.6699525,130.6226508)
        p7 = lp.SearchablePoint(47.51849234497187, -122.29882795153917)
        p8 = lp.SearchablePoint(47.13881656688995, -122.46299580015643)
        p9 = lp.SearchablePoint(47.18524082238581, -122.56227739052319)
        origin_point = lp.SearchablePoint(47.6756757, -122.3949482)
        lst = LocationSearchTree(3)
        lst.add_location_points([p0, p1, p2, p3, p4, p5, p6, p7, p8, p9])
        nn = lst.get_nearest_neighbors(origin_point, 2)
        self.assertEqual(2, len(nn))
        self.assertEqual(p3, nn[0])
        self.assertEqual(p1, nn[1])


