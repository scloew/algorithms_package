from datetime import datetime #, timedelta


def daysBetweenDates(self, date1: str, date2: str) -> int:
    yr1, month1, day1 = (int(i) for i in date1.split('-'))
    yr2, month2, day2 = (int(i) for i in date2.split('-'))
    temp1 = datetime(year=yr1, month=month1, day=day1)
    temp2 = datetime(year=yr2, month=month2, day=day2)
    ret = (temp1 - temp2).days
    return ret if ret > 0 else -ret
