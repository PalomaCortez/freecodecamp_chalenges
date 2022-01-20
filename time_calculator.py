# This code is related to the Time Calculator Chalenge. The description of the requirements are on the link bellow
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

def add_time(start, duration, week_day=None ):
    # time is in "hh:mm 12h" there is no second session.
    
    # calling a time converter function to have everything in minutes
    time0 = time_2_minute(start)
    time_add = time_2_minute(duration)
    final_time = time0 + time_add
    
    # converting back to hh:mm 12h
    hours = int(final_time//60)
    minutes = final_time%60
    
    days = hours//24
    hh = hours%24
    
    # getting the number of extra days    
    extra_days = ""
    if hours >= 24:
        if days == 1:
            extra_days = " (next day)"
        else:
            extra_days = f" ({days} days later)"
    
    # setting to 12h format
    if hh > 12:
        hh -= 12
        meridiem_set = 'PM'
    elif hh == 12:
        meridiem_set = 'PM'
    else:
        meridiem_set = 'AM'
        
    if hh == 0:
        hh = 12
    
    # handling the day of the week option
    end_day = ""
    if week_day is not None:
        # setting weekdays:
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        weekd = week_day.capitalize()
        week_index = weekdays.index(weekd)

        future_index = ((week_index + days)%7)  # must avoid index errors
        end_day = ", " + weekdays[future_index]          
        
    # formating text
    sh = f"{hh}"
#     if len(sh) == 1:
#         sh = "0"+sh    
    
    sm = f"{minutes}"
    if len(sm) == 1:
        sm = "0"+sm

    new_time = f"{sh}:{sm} {meridiem_set}{end_day}{extra_days}"

    return new_time

def time_2_minute(time):
    
    # time is in "hh:mm 12h" there is no second session.
    # in onder to cenvert time without iporting libraries, we can replace the space
    # to have one single separator.
    time = time.replace(' ',':')
    parts = time.split(':')
    
    # for convenience, seting the clock for 24h
    try:
        if parts[2] == 'PM':
            parts[2] = 12*60
        else:
          parts[2] = 0
            
    except IndexError:
        pass
    
        
    # converting all to minutes and ints
    parts[0] = int(parts[0])*60
    parts[1] = int(parts[1])
    time_min = sum(parts)
    
    return time_min
