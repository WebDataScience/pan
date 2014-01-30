import os

#calculate the number of days between two days
def daysInBetween(d1, d2):
    #d1 = datetime.strptime(d1, "%Y-%m-%d")
    # d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)  


#Extract the hous from the time format
def extractHour(time_format):
    #date format: 09/08/12 11:23:45 or 11:23
    dates = time_format.split('/')
    day=dates[0]
    month=dates[1]
    yearHour=dates[2].split(':')
    formats = yearHour[0].split(' ')
    year = formats[0]
    hour = formats[1]
    if yearHour[1].find('PM') <>-1:
        hourTime = int(hour) +12
        hour = str(hourTime)
    return hour, year, month, day

#Extract the time slot which user post the blog post
def ExtractTimeSlot(timeLable):
    time = int(timeLable)
    if time<=6:
        morning = 0
        afternoon=0
        evening=0
        night=0
        midNight =1
    elif time>6 and time<=11:
        morning = 1
        afternoon=0
        evening=0
        night=0
        midNight =0
    elif time>11 and time<=16:
        morning = 0
        afternoon=1
        evening=0
        night=0
        midNight =0
    elif time>16 and time<=21:
        morning = 0
        afternoon=0
        evening=1
        night=0
        midNight =0
    else:
    #if time>21 and time<0:
        morning = 0
        afternoon=0
        evening=0
        night=1
        midNight =0
    return morning, afternoon, evening,night,midNight