class PlayerRecord:
    def __init__(self,inPlayerName,inSalary,inYear,inLeague):
        self.playerName = inPlayerName
        self.salary = inSalary
        self.year = inYear
        self.league = inLeague

    def __str__(self):
        return "Name: "+self.playerName+" Salary: "+self.salary
