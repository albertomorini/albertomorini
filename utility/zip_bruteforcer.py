import itertools
from itertools import product
import py7zr
import sys

filename = sys.argv[1]

def openArchive(password):
    try:
        with py7zr.SevenZipFile(filename, mode='r',password='Test') as z:
            z.extractall()
        return True
    except Exception as e:
        return False


def start():
    chars = 'abcdefghilmnopqtrsuvzhjy,.@()!' # chars to look for

    for length in range(4, len(chars)): # only do lengths of 1 + 2
        to_attempt = product(chars, repeat=length)
        for attempt in to_attempt:
            if(openArchive(''.join(attempt))):
                print(''.join(attempt))
                break

start()