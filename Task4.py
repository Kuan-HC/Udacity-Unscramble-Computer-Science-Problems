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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def marketingNum(texts, calls):
    # possible  telephone marketing -> do not consider phone numbers start with 140
    phoneSetIn = set()
    phoneSetOut = set()

    for num_1, num_2, time in texts:
        phoneSetIn.add(num_1)
        phoneSetIn.add(num_2)

    for num_1, num_2, time, last in calls:
        phoneSetOut.add(num_1)
        phoneSetIn.add(num_2)


    candidate = phoneSetOut.difference(phoneSetIn)
    phoneList = list(candidate)
    phoneList.sort()

    print("These numbers could be telemarketers: ")
    for phone in phoneList:
        print(phone)

marketingNum(texts, calls)
