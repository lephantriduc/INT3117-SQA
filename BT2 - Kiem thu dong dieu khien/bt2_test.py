import unittest
from gross_to_net_post_2026 import gross_to_net, Region

class TestGrossToNetC2(unittest.TestCase):
    """ Kiem thu voi do do C2 """

    def test_bva_01(self):
        with self.assertRaises(ValueError):
            gross_to_net(20000000, 99, 1000000, Region.III)

    def test_bva_02(self):
        self.assertEqual(gross_to_net(3000000, 1, 5310000, Region.I), 2442450)

    def test_bva_03(self):
        self.assertEqual(gross_to_net(150000000, 3, 7000000, Region.II), 123457250)

if __name__ == "__main__":
    unittest.main()
