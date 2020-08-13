import unittest

from src.data.PlayerRecord import PlayerRecord


class PlayerRecordTests(unittest.TestCase):
    def test_GivenNameIsNone_ThenReturnFalse(self):
        expected = False
        classUnderTest = PlayerRecord(None,"5,000,000","2020","MLB")
        actual = classUnderTest.isValid()
        self.assertEqual(expected, actual)

    def test_GivenSalaryIsNone_ThenReturnFalse(self):
        expected = False
        classUnderTest = PlayerRecord("Fee,Craig", None, "2020", "MLB")
        actual = classUnderTest.isValid()
        self.assertEqual(expected, actual)

    def test_GivenYearIsNone_ThenReturnFalse(self):
        expected = False
        classUnderTest = PlayerRecord("Fee,Craig", "2345234", None, "MLB")
        actual = classUnderTest.isValid()
        self.assertEqual(expected, actual)

    def test_GivenLeagueIsNone_ThenReturnFalse(self):
        expected = False
        classUnderTest = PlayerRecord("Fee,Craig", "2345234", "2016", "")
        actual = classUnderTest.isValid()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
