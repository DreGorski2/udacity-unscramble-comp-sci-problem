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


def unique_calls(calls):
    total_calls = set()
    for call in calls:
        total_calls.add(call[0])
        total_calls.add(call[1])
    return total_calls


def unique_texts(texts):
    total_texts = set()
    for text in texts:
        total_texts.add(text[0])
        total_texts.add(text[1])
    return total_texts


def messaging(total_calls, total_texts):
    print(f'''There are {len(total_texts.union(total_calls))} different telephone numbers in the records.''')


if __name__ == '__main__':
    texts = text_data(path)
    calls = call_data(path)
    total_texts = unique_texts(texts)
    total_calls = unique_calls(calls)
    messaging(total_texts, total_calls)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


