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


def parse_marketer_calls(calls):
    out_call= set()
    no_tele = set()
    for call in calls:
        out_call.add(call[0])
        no_tele.add(call[1])
    return out_call, no_tele


def parse_marketer_text(texts, no_tele):
    for text in texts:
        no_tele.add(text[0])
        no_tele.add(text[1])
    return no_tele


def compare(out_call, no_tele):
    tele = list(out_call - no_tele)
    return tele
        

def display_numbers(tele):
    print("These numbers could be telemarketers: \n")
    tele.sort()
    print(*tele, sep="\n")


if __name__ == '__main__':
    texts = text_data(path)
    calls = call_data(path)
    out_call, no_tele = parse_marketer_calls(calls)
    no_tele = parse_marketer_text(texts, no_tele)
    tele = compare(out_call, no_tele)
    display_numbers(tele)


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
