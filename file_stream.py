from csv import DictReader
from collections.abc import Iterator
from pathlib import Path



def process_row(row):
    pass

def read_row(path: Path) -> Iterator[dict]:
    with open(path, newline='', endcoding='UTF-8') as f:
        yield from DictReader(f)


reader = read_row('some_file_path')

try:
    for row in reader:
        if row['status'] == 'STOP':
            break
        process_row(row)
finally:
    reader.close()
