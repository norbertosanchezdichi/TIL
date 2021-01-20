def week():
    daysInWeek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in daysInWeek:
        yield day
        
days = week()
print(next(days)) # 'Monday'
print(next(days)) # 'Tuesday'
print(next(days)) # 'Wednesday'
print(next(days)) # 'Thursday'
print(next(days)) # 'Friday'
print(next(days)) # 'Saturday'
print(next(days)) # 'Sunday'
print(next(days)) # StopIteration