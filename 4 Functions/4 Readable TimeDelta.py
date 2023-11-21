def readable_timedelta(days):
    weeks  = days // 7 #i.e, the rounded down nearest whole number
    remainder = days % 7
    return "{} week(s) and {} days(s).".format(weeks,remainder)

print(readable_timedelta(10))
    