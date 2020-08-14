class QualifyingOfferController:
    def __init__(self, inHtmlWrapper):
        self.htmlWrapper = inHtmlWrapper
        self.records = []

    def determineQualifyingOffer(self):
        self.records = self.htmlWrapper.getSalaryDataFromHtmlTable()
        self.cleanData()
        for i in self.records:
            print(i)
        #REFERENCE https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
        self.records.sort(key=lambda record: record.salary, reverse=True)
        offerValue = self.averageTop125Salaries()
        #REFERENCE https://www.kite.com/python/answers/how-to-format-currency-in-python
        offerValueAsCurrency = "${:,}".format(offerValue)
        return offerValueAsCurrency

    def cleanData(self):
        for record in self.records:
            if not record.isValid():
                print("Player: "+record.playerName+"is invalid")
                self.records.remove(record)



    def averageTop125Salaries(self):
        sumOfTop125Salaries = 0
        for index in range(125):
            print(self.records[index].salary)
            sumOfTop125Salaries += int(self.records[index].salary)
        return sumOfTop125Salaries // 125
