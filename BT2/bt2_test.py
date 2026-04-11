import unittest
from gross_to_net.gross_to_net_post_2026 import gross_to_net, Region

class TestGrossToNetC2(unittest.TestCase):
    """ Kiểm thử với độ đo C2 """

    def test_c2_01(self):
        with self.assertRaises(ValueError):
            gross_to_net(20000000, 99, 1000000, Region.III)

    def test_c2_02(self):
        self.assertEqual(gross_to_net(3000000, 1, 5310000, Region.I), 2442450)

    def test_c2_03(self):
        self.assertEqual(gross_to_net(150000000, 3, 7000000, Region.II), 123457250)

if __name__ == "__main__":
    unittest.main()
