import logging

from bot.util import Keys



class BotLogger(logging.Logger):
    fh = logging.FileHandler(Keys.LOG_FILE)
    formatter = logging.Formatter("%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    def __init__(self, name: str, level = logging.DEBUG) -> None:
        super().__init__(name, level)
        self.addHandler(self.fh)
        self.addHandler(self.ch)

        
