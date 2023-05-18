#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
ISO_8859_1,  iso-8859-1, utf-8-xxx
"""
def _get_normal_name(orig_enc):
    # Only care about the first 12 characters.
    enc = orig_enc[:12].lower().replace("_", "-")
    if enc == "utf-8" or enc.startswith("utf-8-"):
        return "utf-8"
    if enc in ("latin-1", "iso-8859-1", "iso-latin-1") or \
       enc.startswith(("latin-1-", "iso-8859-1-", "iso-latin-1-")):
        return "iso-8859-1"
    return orig_enc

def parse_config(text):
    for line in text.splitlines():
        if '=' in line:
            i = line.index('=')
            key, value = line[:i], line[i+1:]
            print('key={} value={}'.format(key.strip(), value.strip()))

def parse_config2(text):
    for line in text.splitlines():
        if '=' in line:
            key, _, value = line.partition('=')
            print('key={} value={}'.format(key.strip(), value.strip()))

def parse_config3(text):
    for line in text.splitlines():
            try:
                i = line.index('=')
            except ValueError:
                pass  # ignore it
            else:
                i = line.index('=')
                key, value = line[:i], line[i+1:]
                print('key={} value={}'.format(key.strip(), value.strip()))

def split_filename(filename=__file__, sep='/'):
    if sep not in filename:
        return '', filename

    i = filename.rindex(sep)
    dirname, basename = filename[:i], filename[i+1:]
    if dirname != sep * len(dirname):
        dirname = dirname.rstrip(sep)
    print('dirname=', dirname)
    print('basename=', basename)
    return dirname, basename

# index 和find的区别
def split_filename1(filename=__file__, sep='/'):
    i = filename.rfind(sep)
    if i == -1:
        return '', filename
    dirname, basename = filename[:i], filename[i+1:]
    if dirname != sep * len(dirname):
        dirname = dirname.rstrip(sep)
    print('dirname=', dirname)
    print('basename=', basename)
    return dirname, basename

def split_filename2(filename=__file__, sep='/'):
    try:
        i = filename.rindex(sep)
    except ValueError:
        dirname, basename = '', filename
    else:
        dirname, basename = filename[:i], filename[i+1:]
        if dirname and dirname != sep * len(dirname):
            dirname = dirname.rstrip(sep)
    print('dirname=', dirname)
    print('basename=', basename)
    return dirname, basename


if __name__ == '__main__':
    text = '''key1=value1
    key2 = value2
    key3 = value3=
    '''

    total_lines = text.count('\n') + (text[-1] != '\n')
    print(total_lines)
    parse_config(text)

    print()
    filename = r'C:\Program Files\Microsoft Office\Office16\winword.exe'
    sep = '\\'

    split_filename(filename, sep)

    print()
    split_filename1(filename, sep)
