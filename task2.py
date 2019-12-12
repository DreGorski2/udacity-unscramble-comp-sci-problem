"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import os
import operator

path = os.getcwd()


def text_data(path):
    with open(path + '/data_files/texts.csv', 'r') as t:
        reader = csv.reader(t)
        texts = list(reader)
    return texts


def call_data(path):
    with open(path + '/data_files/calls.csv', 'r') as c:
        reader = csv.reader(c)
        calls = list(reader)
    return calls


def find_calls_sept(calls):
    sept_calls = []
    for call in calls:
        if call[2][3:5] == '09' and call[2][8:10] == '16':
            data = {
                "caller": call[0],
                "receiver": call[1],
                "time_stamp": call[2],
                "duration": int(call[3])
            }
            sept_calls.append(data)
    return sept_calls


def get_duration_caller(sept_calls):
    callers = {}
    for call in sept_calls:
        if call['caller'] not in callers:
            callers[call['caller']] = call['duration']
        else:
            callers[call['caller']] = callers[call['caller']] + call['duration']
    return callers


def get_duration_receiver(sept_calls, callers):
    for call in sept_calls:
        if call['receiver'] not in callers:
            callers[call['receiver']] = call['duration']
        else:
            callers[call['receiver']] = callers[call['receiver']] + call['duration']
    return callers


def display_caller(callers):
    number = max(callers.items(), key=operator.itemgetter(1))[0]
    print(f'''{number} spent the longest time, {callers[number]} seconds, on the phone during September 2016.''')


if __name__ == '__main__':
    texts = text_data(path)
    calls = call_data(path)
    sept_calls = find_calls_sept(calls)
    callers = get_duration_caller(sept_calls)
    callers = get_duration_receiver(sept_calls, callers)
    display_caller(callers)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""



