# Class: HtmlWrapper will handle all of the application interactions involving html and
# will have the knowledge to return any data as a simple and useable data structure
import re

import lxml.html as htmlParser
# REFERENCE: https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059
# Used for accessing html objects
import requests

from src.data.PlayerRecord import PlayerRecord


class HtmlWrapper:

    def getSalaryDataFromHtmlTable(self):
        url = 'https://questionnaire-148920.appspot.com/swe/data.html'
        page = requests.get(url)
        doc = htmlParser.fromstring(page.content)
        playerRecords = doc.xpath('//tr')

        translatedRecords = []

        for player in playerRecords:
            name = ""
            salary = ""
            year = ""
            league = ""

            if (None != player[0]):
                name = player[0].text_content()

            if (None != player[1]):
                unformattedSalary = player[1].text_content()
                salary = currencyToInteger(unformattedSalary)
            if (None != player[2]):
                year = player[2].text_content()

            if (None != player[3]):
                league = player[3].text_content()

            newplayer = PlayerRecord(name, salary, year, player)
            print(newplayer)
            translatedRecords.append(newplayer)

        print(len(translatedRecords))
        return translatedRecords

    # REFERENCE: https://stackoverflow.com/questions/875968/how-to-remove-symbols-from-a-string-with-python
    # How to format a string to have no symbols
    def currencyToInteger(self,salarystring):
        return re.sub(r'[^\d]', '', salarystring)
