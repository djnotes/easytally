from enum import Enum
import re
from bot.logger import BotLogger

from bot.util import digitize

class ReportType(Enum):
    COST = 0
    INCOME = 1
    INVALID = 2



class Report:
    costPat = r"^(?P<value>\d+)\s{0,2}تومان\s{0,2}برداشت\s(?P<description>.*)$"
    incomePat = r"^(?P<value>\d+)\s{0,2}تومان\s{0,2}واریز\s(?P<description>.*)$"
    def __init__(self, text: str):
        self.logger = BotLogger(__name__)
        self.logger.info(f'Processing {text}')
        self.type = ReportType.INVALID
        self.value = None
        self.description = None

        self.text = text
        if self.text is None:
            return
        costMatch = re.search(self.costPat, text)
        if costMatch:
            self.type = ReportType.COST
            self.value = digitize(costMatch.group('value'))
            self.description = costMatch.group('description')
        else:
            incomeMatch = re.search(self.incomePat, text)
            if incomeMatch:
                self.type = ReportType.INCOME
                self.value = digitize(incomeMatch.group('value'))
                self.description = incomeMatch.group('description')
        self.logger.info(f'Report type for {text}: {self.type.name}')      
        
        
    