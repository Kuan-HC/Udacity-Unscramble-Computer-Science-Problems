"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def differentNum(texts, calls):
    telephoneSet = set()
    for num_1, num_2, time in texts:
        telephoneSet.add(num_1)
        telephoneSet.add(num_2)

    for num_1, num_2, time, last in calls:
        telephoneSet.add(num_1)
        telephoneSet.add(num_2)

    print("There are %i different telephone numbers in the records." %len(telephoneSet))

differentNum(texts, calls)  
