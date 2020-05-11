import unittest

class SampleTests(unittest.TestCase):

    def test_1(self):
        """assertTrue"""
        self.assertTrue(True)

    def test_2(self):
        """assert false"""
        self.assertFalse(False)

    def test_8(self):
        """Check equal."""
        self.assertEqual(2, (4/2))

    def test_11(self):
        """Check not equal."""
        self.assertNotEqual(3, 11)

    def test_25(self):
        """Check array contains element."""
        arr = [1, 2, 3, 4, 5]

        self.assertIn(arr, 1)

    def test_28(self):
        """Check element not in array."""
        arr = [1, 2, 3, 4, 5]
        self.assertNotIn(arr, 20)

if __name__ == "__main__":
    unittest.main()
