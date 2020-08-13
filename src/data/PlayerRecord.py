class PlayerRecord:
    def __init__(self,inPlayerName,inSalary,inYear,inLeague):
        self.playerName = inPlayerName
        self.salary = inSalary
        self.year = inYear
        self.league = inLeague

    def __str__(self):
        return "Name: " + self.playerName + " Salary: " + str(self.salary)

    def isValid(self):
        if self.playerName is None:
            return False
        if self.salary is None:
            return False
        if self.year is None:
            return False
        if self.league is None:
            return False
        return True


