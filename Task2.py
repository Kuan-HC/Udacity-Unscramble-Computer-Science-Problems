"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longestCall(calls):
    # accumulte the time each phone number spend
    timeMap = {}
    longestTime = 0
    longestPhone = None

    for num_1, num_2, time, last in calls:
        if num_1 in timeMap:
            timeMap[num_1] += int(last)
        else:
            timeMap[num_1] = int(last)
        
        if timeMap[num_1] > longestTime:
            longestPhone = num_1
            longestTime = timeMap[num_1]

        if num_2 in timeMap:
            timeMap[num_2] += int(last)
        else:
            timeMap[num_2] = int(last)

        if timeMap[num_2] > longestTime:
            longestPhone = num_2
            longestTime = timeMap[num_2]
    
    print("%s spent the longest time, %i seconds, on the phone during September 2016." %(longestPhone, longestTime))

longestCall(calls)