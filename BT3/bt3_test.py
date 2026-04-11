import unittest
from gross_to_net.gross_to_net_post_2026 import gross_to_net, Region

class TestGrossToAllUses(unittest.TestCase):
    """ Kiem thu voi do do all-uses """

    def test_au_01(self):
        with self.assertRaises(ValueError):
            gross_to_net(20000000, 999, 5000000, Region.IV)

    def test_au_02(self):
        self.assertEqual(gross_to_net(10000000, 3, 5310000, Region.I), 9442450)

    def test_au_03(self):
        self.assertEqual(gross_to_net(130000000, 2, 4140000, Region.III), 108482445)

if __name__ == "__main__":
    unittest.main()
