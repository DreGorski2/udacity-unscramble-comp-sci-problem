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
    call_marketers = list(set([call[0] for call in calls if call[0][0:3] == '140' and call[0] not in calls[1]]))
    return call_marketers


def parse_marketers_text(texts):
    text_marketers = list(set(text[0] for text in texts if text[0][0:3] == '140' and text[0] not in texts[1]))
    return text_marketers


def compare(call_marketers, text_marketers):
    final_list = []
    for call in call_marketers:
        if call not in text_marketers:
            final_list.append(call)
    return final_list


def display_numbers(final_list):
    print("These numbers could be telemarketers: \n")
    final_list.sort()
    print(*final_list, sep="\n")


if __name__ == '__main__':
    texts = text_data(path)
    calls = call_data(path)
    call_marketers = parse_marketer_calls(calls)
    text_marketers = parse_marketers_text(texts)
    final_list = compare(call_marketers, text_marketers)
    display_numbers(final_list)


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
