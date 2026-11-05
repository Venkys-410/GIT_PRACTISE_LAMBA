from itertools import islice
from pathlib import Path
from contextlib import closing
import csv


def read_rows(file):
    with open(Path(file), newline='') as f:
        yield from csv.reader(f)

def batched(iterable, n):
    if n<1:
        raise ValueError("Batch Size must be greater than 1")
    it = iter(iterable)
    while batch:=list(islice(it,n)):
        yield batch


with closing(read_rows('some_file')) as reader:
    for batch in batched(reader, 5000):
        pass