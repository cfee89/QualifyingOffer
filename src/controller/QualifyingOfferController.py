class QualifyingOfferController:
    def __init__(self, inHtmlWrapper):
        self.htmlWrapper = inHtmlWrapper

    def determineQualifyingOffer(self):
        records = self.htmlWrapper.getSalaryDataFromHtmlTable()
        self.cleanData(records)
        records.sort(key=lambda record:record.salary)
        return self.averageTop125Salaries(records)

    def cleanData(self,inRecords):
        for record in inRecords:
            if not record.isValid():
                inRecords.remove(record)

    def averageTop125Salaries(self,inRecords):
        sumOfTop125Salaries = 0
        for index in range(125):
            sumOfTop125Salaries+= int(inRecords[index].salary)
        return sumOfTop125Salaries//125

