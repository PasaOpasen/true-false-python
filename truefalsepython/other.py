



def time_to_seconds(days: int = 0, hours:int = 0, minutes:int = 0, seconds: float = 5):
    """
    Converts argument's time to pure seconds
    """
    
    hours = hours + 24*days

    minutes = minutes + 60*hours

    seconds = seconds + 60*minutes

    return seconds


