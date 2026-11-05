from csv import DictReader
from contextlib import closing
from pathlib import Path

def parse_rows(rows):
    for row in rows:
        try:
            yield {**row, "rent":int(row["rent"])}
        except(ValueError, TypeError):
            continue

def rent_pending(rows):
    return (r for r in rows if r["paid"]=='N')

def total_rent(rows):
    return sum(r["rent"] for r in rows)

def read_rows(path):
    with open(path, newline='', encoding='uff-8') as f:
        yield from DictReader(f)


def main():
    file_path = Path('some_file_path')

    with closing(read_rows(file_path)) as reader:
        result = total_rent(rent_pending(parse_rows(reader)))

    print(result)



if __name__=="__main__":
    main()

    
        


