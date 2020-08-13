import unittest
from unittest.mock import MagicMock

from src.controller.QualifyingOfferController import QualifyingOfferController
from src.data.PlayerRecord import PlayerRecord
from src.servicewrappers.HtmlWrapper import HtmlWrapper

class QualifyingOfferControllerTest(unittest.TestCase):
    def test_GivenValidData_WhenDetermineQualifyingOffer_ThenReturnValidIntegerAverage(self):
        #setup preconditions
        expectedOfferValue = 7624682
        validPlayerRecord =[]
        for index in range(25):
            validPlayerRecord.append(PlayerRecord("Fee,Craig", "123414", "2016", "MLB"))
            validPlayerRecord.append(PlayerRecord("Chooch", "23000000", "2016", "MLB"))
            validPlayerRecord.append(PlayerRecord("Frenetic, Philly", "5000000", "2016", "MLB"))
            validPlayerRecord.append(PlayerRecord("Fanatic, Philly", "5000000", "2016", "MLB"))
            validPlayerRecord.append(PlayerRecord("Utley, Chase", "5000000", "2016", "MLB"))

        mockHtmlWrapper = HtmlWrapper()
        mockHtmlWrapper.getSalaryDataFromHtmlTable = MagicMock(return_value = validPlayerRecord)
        #initialize class under test
        classUnderTest = QualifyingOfferController(mockHtmlWrapper)

        #act
        actualOfferValue = classUnderTest.determineQualifyingOffer()

        #postconditions
        self.assertEqual(expectedOfferValue,actualOfferValue)

if __name__ == '__main__':
    unittest.main()
