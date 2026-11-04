from csv import DictReader
from collections.abc import Iterator
from pathlib import Path
from contextlib import closing



def process_row(row):
    pass

def read_row(path: Path) -> Iterator[dict]:
    with open(path, newline='', endcoding='UTF-8') as f:
        yield from DictReader(f)


# reader = read_row('some_file_path')

#own style
'''
try:
    for row in reader:
        if row['status'] == 'STOP':
            break
        process_row(row)
finally:
    reader.close()
'''
#refined style

with closing(read_row(Path('some_file_path'))) as reader:
    for row in reader:
        process_row(row)