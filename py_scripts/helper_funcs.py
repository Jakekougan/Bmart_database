import random


def upc_gen(n):
    '''Generates a given number of upc codes

    Parameters:
        n (int): amount of random upcs

    Returns:
        None '''

    while n > 0:
        codes = set()
        upc = ""
        for i in range(12):
            upc += str(random.randint(0,9))
        if upc not in codes:
            print("'"+upc+"'")
            n -=1


def days_in_month(month):
    month = int(month)
    if month not in range(1,12):
         return 0
    calendar = {1 : 31,
                2 : 28,
                3 : 31,
                4 : 30,
                5 : 31,
                6 : 30,
                7 : 31,
                8 : 31,
                9 : 30,
                10 : 31,
                11 : 30,
                12 : 31}
    return calendar.get(month)


def date_plus(date, days_forward):
    date = (int(date[0]), int(date[1]), int(date[2]) )
    month : int = date[0]
    yr : int = date[2]

    days_per_month : int = days_in_month(month) # type: ignore
    day : int = date[1]

    for i in range(1, days_forward + 1): # type: ignore
            day += 1
            days_forward -=1

            #in case the amount of days in the given month is surpassed, go to next month
            if day >= days_per_month:
                month += 1
                day = 1
                days_forward -= 1
                days_per_month = days_in_month(month) # type: ignore

                #if we are about to pass december go back to january
                if month > 12:
                     month = 1
                     yr += 1

    return str(month) +"-" + str(day) + "-" + str(yr)


print(date_plus((4,18, 2025), 20))