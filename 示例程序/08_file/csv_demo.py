import csv

def csv_reader1():
    text='''name,memo
    dlmao,just a test
    dlmao,just a test,others
    "Dilin, Mao","""it's a test"""
    '''
    reader = csv.reader(text.splitlines())
    for row in reader:
        print(row)

def print_file(file):
    print('-' * 20 + file + '-' * 20 )
    with open(file) as f:
        print(f.read(), end='')
    print('-' * 50)

def csv_writer(file='eggs.csv'):
    with open(file, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    print_file(file)


def csv_reader(file='eggs.csv'):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print(', '.join(row))

def dict_writer(file='names.csv'):
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    print_file(file)

def dict_reader(file='names.csv'):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])

if __name__ == '__main__':
    for dialect in csv.list_dialects():
        dialect_obj = csv.get_dialect(dialect)
        print('settings %s:' % dialect)
        settings = {item:getattr(dialect_obj, item) for item in dir(dialect_obj) if not item.startswith('_')}
        print(settings)

    csv_reader1()

    csv_writer('eggs.csv')
    csv_reader('eggs.csv')

    dict_writer('names.csv')
    dict_reader('names.csv')
