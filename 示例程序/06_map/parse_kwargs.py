#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def parse_options(**kwargs):
    print(kwargs)
    verbose = kwargs.pop('verbose', False)
    reverse = kwargs.pop('reverse', False)
    key = kwargs.pop('key', None)
    while len(kwargs):
        option, value = kwargs.popitem()
        print('unknown option:%s=%s' % (option, value))


def check_options(**kwargs):
    valid_options = {'verbose', 'reverse', 'key'}
    unknown_options = set(kwargs) - valid_options
    if len(unknown_options):
        print('unknown options:', *unknown_options)


if __name__ == '__main__':
    options = {'reverse':True, 'key':lambda item:item[0], 'option1':1, 'option2':2}
    check_options(**options)
    parse_options(**options)
