import io

def stringio_demo():
    file = io.StringIO("line 1\nline 2\n")
    while True:
        line = file.read()
        if not line:
            break
        print(line, end='')
    file.write("line 3\nline 4\n")
    print(file.getvalue())
    file.seek(0)
    for line in file:
        print(line, end='')

def bytesio_demo():
    file = io.BytesIO()
    file.write(b"line 1\nline 2\n")
    print(file.getvalue())

if __name__ == '__main__':
    stringio_demo()
    print()
    bytesio_demo()
