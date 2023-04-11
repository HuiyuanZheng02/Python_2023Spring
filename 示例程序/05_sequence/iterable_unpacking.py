#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def test_iterable_unpacking():
    data = ['Tom', 'math', '16010045', '13905750074', (1999, 12, 21)]
    name, major, _, phone, birth = data
    print(name, major, phone, birth)

    s = list(range(10))
    print(*s, sep=' + ', end=' = ')
    print(sum(s))


    import random
    lst = list(range(20))
    random.shuffle(lst)
    print('lst=', *lst)

    sorted_rule1 = {'key': lambda item: len(str(item)), 'reverse': True}
    sorted_rule2 = {'key': None, 'reverse': True}
    print(*sorted(lst, **sorted_rule1))
    print(*sorted(lst, **sorted_rule2))

    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record
    print(name, email, phone_numbers)

    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    # uname, *fields, homedir, sh = line.split(':')
    user = line.split(':')
    print(user)
    uname, *fields, homedir, sh = user
    print(uname, homedir, sh)


if __name__ == '__main__':
    test_iterable_unpacking()
