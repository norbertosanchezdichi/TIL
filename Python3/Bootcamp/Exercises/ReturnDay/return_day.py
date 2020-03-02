def return_day(number):
    day_of_the_week = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
    
    return day_of_the_week.get(number, None)
    
print(return_day(6))
print(return_day())