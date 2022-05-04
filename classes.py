from enum import Enum
import re

class ReportType(Enum):
    EXPENSE = 0
    INCOME = 1
    INVALID = 2



class Report:
    expensePattern = r"^(?P<value>\d+)\s{0,2}تومان\s{0,2}برداشت\w+"
    incomePattern = r"^(?P<value>\d+)\s{0,2}تومان\s{0,2}واریز\w+"
    def __init__(self, text: str):
        self.text = text
        expenseMatch = re.search(self.expensePattern, text)
        if expenseMatch:
            self.type = ReportType.EXPENSE
            self.value = expenseMatch.group('value')
        else:
            incomeMatch = re.search(self.incomePattern, text)
            if incomeMatch:
                self.type = ReportType.INCOME
                self.value = incomeMatch.group('value')
        
        if not self.type:
            # If no pattern matches, it is considered invalid report
            self.type = ReportType.INVALID
        
    