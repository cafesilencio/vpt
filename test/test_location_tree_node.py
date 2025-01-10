import unittest
import location_tree_node as ltn
from internal import support
from location_point import SearchablePoint

class LocationTreeNodeTests(unittest.TestCase):

    def test_initialization(self):
        points = [
            SearchablePoint(34.4385004718802, 135.26354888814373),
            SearchablePoint(34.4348974768167,135.26729722216783),
            SearchablePoint(34.4316918077749,135.27143269522125),
            SearchablePoint(34.4286170052391,135.27550312908502),
            SearchablePoint(34.42554206785929,135.2795732634925),
            SearchablePoint(34.4224669956609,135.28364309848703),
            SearchablePoint(34.4193917886693,135.28771263411198),
            SearchablePoint(34.41631644691015,135.2917818704107)
        ]
        distance_calc_fun = support.distance_calc_haversine
        node = ltn.LocationTreeNode(points, distance_calc_fun, 3)
        self.assertEqual(node.size(), 3)
        self.assertEqual(node.closer.size(), 2)
        self.assertEqual(node.farther.size(), 3)

    def test_initialization2(self):
        points = [
            SearchablePoint(34.4385004718802, 135.26354888814373),
            SearchablePoint(34.4348974768167,135.26729722216783),
            SearchablePoint(34.4316918077749,135.27143269522125),
            SearchablePoint(34.4286170052391,135.27550312908502),
            SearchablePoint(34.42554206785929,135.2795732634925),
            SearchablePoint(34.4224669956609,135.28364309848703),
            SearchablePoint(34.4193917886693,135.28771263411198),
            SearchablePoint(34.41631644691015,135.2917818704107)
        ]
        distance_calc_fun = support.distance_calc_haversine
        node = ltn.LocationTreeNode(points, distance_calc_fun, 6)
        self.assertEqual(node.size(), 5)
        self.assertIsNone(node.closer)
        self.assertEqual(node.farther.size(), 3)