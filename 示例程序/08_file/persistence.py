#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import pickle
import shelve
import json

def pickle_dump(file='pickle.dat'):
    with open(file, 'wb') as f:
        n1 = 1024
        f1 = 3.14
        c1 = 1 + 2j
        s1 = 'python程序设计'
        l1 = [1,2,3]
        l2 = [l1, l1, 4, 5]
        t1 = 4, 5, 6
        st1 = {1, 2, 3}
        d1 = {'name':'idle', 'phone':['10010', '10011']}
        for obj in n1, f1, c1, s1, l1, l2, t1, st1, d1:
            pickle.dump(obj, f)

def pickle_load(file='pickle.dat'):
    with open(file, 'rb') as f:
        while True:
            try:
                obj = pickle.load(f)
                print(obj)
            except EOFError:
                break


def json_demo(file='demo.json'):
    text = r"""
{
    "editor.minimap.enabled": true,
    "editor.wordWrap": 124,
    "python.pythonPath": "D:\\python3",
    "args": ["--quiet", "--norepeat", "--port", "1593"],
    "vim.handleKeys": {
        "<C-n>": false
    }
}
    """
    config = json.loads(text)
    print(config)

    with open(file, 'w') as f:
        json.dump(config, f, indent=4)



if __name__ == '__main__':
    pickle_dump()
    pickle_load()

    print()

    json_demo()
