print('input a date in format (dd/mm/yyyy)')
proposed_date = '02/02/2000'
import re


def valid_date(date):
    ends_with_slash = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    split_date = ends_with_slash.search(date)
    day = int(split_date.group(1))
    month = int(split_date.group(2))
    year = int(split_date.group(3))
    days_30 = [4,6,9,11]
    days_31 = [1,3,5,7,8,10]
    if (0 < day <= 31):
        if (month < 13):
            if month in days_30 and (day < 31):
                return valid_year(year)
            if (month in days_31) and (day < 32):
                return valid_year(year)    
            if (month == 2):
                if (day <= 28):
                    return valid_year(year)
                if (day == 29):
                    if (year%4 == 0) and (year%100 != 0):
                        return valid_year(year)
                    if (year%400 == 0) and (year%100 == 0):
                        return valid_year(year)

    return False


def valid_year(year):
    if ( 1000 < year < 2999):
        return True 


print(valid_date(proposed_date))
