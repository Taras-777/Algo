import unittest
from main import KMPSearch


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(KMPSearch("ABABCABAB","ABABDABACDABABCABAB"), None)

    def test(self):
        self.assertEqual(KMPSearch("BAABABCA", "CDBAABABCA"), None)


if __name__ == "__main__":
    unittest.main()