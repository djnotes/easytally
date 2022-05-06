DIGITS = {
    "۰":"0",
    "۱":"1",
    "۲":"2",
    "۳":"3",
    "۴":"4",
    "۵":"5",
    "۶":"6",
    "۷":"7",
    "۸":"8",
    "۹":"9",
    "٤":"4",
    "٥":"5",
    "٦":"6",
}

class Keys:
    API_ID = "API_ID"
    API_HASH = "API_HASH"
    BOT_TOKEN = "BOT_TOKEN"
    

class Commands:
    START = "start"
    COST = "cost"
    
def digitize(text: str) -> str:
    """
    Convert Persian (e.g. ۴) and Eastern Arabic (e.g. ٤) digits inside text to Latin numbers  
    """ 
    temp = ""   
    for ch in text:
        temp += DIGITS[ch] if ch in DIGITS else ch

    return temp

