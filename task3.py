"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os

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


def bangalore_calls(calls):
    bangalore_callers = [call for call in calls if call[0][0:5] == '(080)']
    return bangalore_callers

def bangalore_both_ways(bangalore_callers):
    bangalore_only = [call for call in bangalore_callers if call[0][0:5] == '(080)' and call[1][0:5] == '(080)']
    return bangalore_only


def find_area_codes(bangalore_callers):
    area_codes = {'fixed': [], 'mobile': [], 'marketer': []}
    for call in bangalore_callers:
        if call[1][0] == '(':
            end_indx = call[1].find(')') + 1
            if call[1][0: end_indx] not in area_codes['fixed']:
                area_codes['fixed'].append(call[1][0:end_indx])
        elif call[1][0] == '7' or'8' or '9':
            if call[1][0:4] not in area_codes['mobile']:
                area_codes['mobile'].append(call[1][0:4])
        elif call[1][0:4] == '140':
            if call[1][0:3] not in area_codes['marketer']:
                area_codes['marketer'].append(call[1][0:3])
    return area_codes


def display_codes(area_codes):
    print("The numbers called by people in Bangalore have codes:")
    area_codes['fixed'].sort()
    area_codes['mobile'].sort()
    area_codes['marketer'].sort()
    print(*area_codes['fixed'], sep="\n")
    print(*area_codes['mobile'], sep="\n")
    if area_codes['marketer'] is None:
        pass
    else:
        print(*area_codes['marketer'], sep="\n")


def bangalore_metrics(bangalore_callers, bangalore_only):
    metrics = round(len(bangalore_only) / len(bangalore_callers) * 100, 2)
    print(f'''{metrics} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.''')


if __name__ == '__main__':
    texts = text_data(path)
    calls = call_data(path)
    callers = bangalore_calls(calls)
    bangalore_only = bangalore_both_ways(callers)
    area_codes = find_area_codes(callers)
    display_codes(area_codes)
    bangalore_metrics(callers, bangalore_only)


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""








