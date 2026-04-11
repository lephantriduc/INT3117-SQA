import unittest
from gross_to_net.gross_to_net_pre_2026 import gross_to_net, Region

class TestGrossToNetBoundary(unittest.TestCase):
    """ Kiem thu gia tri bien """

    def test_bva_01(self):
        with self.assertRaises(ValueError):
            gross_to_net(-1, 2, 5000000, Region.I)

    def test_bva_02(self):
        self.assertEqual(gross_to_net(0, 2, 5000000, Region.I), -525000)

    def test_bva_03(self):
        self.assertEqual(gross_to_net(1, 2, 5000000, Region.I), -524999)

    def test_bva_04(self):
        self.assertAlmostEqual(gross_to_net(2**64 - 2, 2, 5000000, Region.I), 11990383647927648256)

    def test_bva_05(self):
        self.assertAlmostEqual(gross_to_net(2**64 - 1, 2, 5000000, Region.I), 11990383647927648256)

    def test_bva_06(self):
        with self.assertRaises(ValueError):
            gross_to_net(2**64, 2, 5000000, Region.I)

    def test_bva_07(self):
        with self.assertRaises(ValueError):
            gross_to_net(30000000, -1, 5000000, Region.I)

    def test_bva_08(self):
        self.assertEqual(gross_to_net(30000000, 0, 5000000, Region.I), 27430000)

    def test_bva_09(self):
        self.assertEqual(gross_to_net(30000000, 1, 5000000, Region.I), 28113750)

    def test_bva_10(self):
        self.assertEqual(gross_to_net(30000000, 9, 5000000, Region.I), 29475000)

    def test_bva_11(self):
        self.assertEqual(gross_to_net(30000000, 10, 5000000, Region.I), 29475000)

    def test_bva_12(self):
        with self.assertRaises(ValueError):
            gross_to_net(30000000, 11, 5000000, Region.I)

    def test_bva_13(self):
        with self.assertRaises(ValueError):
            gross_to_net(30000000, 2, 3449999, Region.IV)

    def test_bva_14(self):
        self.assertEqual(gross_to_net(30000000, 2, 3450000, Region.IV), 28903975)

    def test_bva_15(self):
        self.assertEqual(gross_to_net(30000000, 2, 3450001, Region.IV), 28903975)

    def test_bva_16(self):
        with self.assertRaises(ValueError):
            gross_to_net(30000000, 2, 3859999, Region.III)

    def test_bva_17(self):
        self.assertEqual(gross_to_net(30000000, 2, 3860000, Region.III), 28865230)

    def test_bva_18(self):
        self.assertEqual(gross_to_net(30000000, 2, 3860001, Region.III), 28865230)

    def test_bva_19(self):
        with self.assertRaises(ValueError):
            gross_to_net(30000000, 2, 4409999, Region.II)

    def test_bva_20(self):
        self.assertEqual(gross_to_net(30000000, 2, 4410000, Region.II), 28813255)

    def test_bva_21(self):
        self.assertEqual(gross_to_net(30000000, 2, 4410001, Region.II), 28813255)

    def test_bva_22(self):
        with self.assertRaises(ValueError):
            gross_to_net(30000000, 2, 4959999, Region.I)

    def test_bva_23(self):
        self.assertEqual(gross_to_net(30000000, 2, 4960000, Region.I), 28761280)

    def test_bva_24(self):
        self.assertEqual(gross_to_net(30000000, 2, 4960001, Region.I), 28761280)

class TestGrossToNetDecisionTable(unittest.TestCase):
    """ Kiem thu bang quyet dinh """

    def test_dt_01(self):
        with self.assertRaises(ValueError):
            gross_to_net(2**65, 2, 500000000, Region.III)

    def test_dt_02(self):
        with self.assertRaises(ValueError):
            gross_to_net(25000000, 20, 3000000, Region.II)

    def test_dt_03(self):
        with self.assertRaises(ValueError):
            gross_to_net(4000000, 2, 4000000, 'IIII')

    def test_dt_04(self):
        self.assertEqual(gross_to_net(35000000, 1, 35000000, Region.I), 29686250)

    def test_dt_05(self):
        self.assertEqual(gross_to_net(5000000, 4, 4500000, Region.II), 4527500)

    def test_dt_06(self):
        self.assertEqual(gross_to_net(10000000, 0, 7000000, Region.III), 9265000)

    def test_dt_07(self):
        self.assertEqual(gross_to_net(9000000, 7, 4000000, Region.IV), 8580000)

    def test_dt_08(self):
        with self.assertRaises(ValueError):
            gross_to_net(20000000, 3, 3000000, Region.III)

if __name__ == "__main__":
    unittest.main()
