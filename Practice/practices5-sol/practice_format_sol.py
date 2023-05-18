#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

"""
字典capital_country给出了各个国家的首都的信息，
分别采用%以及format来产生类似的输出,其中Country和Capital的宽度填充到至少为20个字符

Country             Capital
----------------------------------------
Netherlands         Amsterdam
Canada              Ottawa
US                  Washington
United States       Washington
England             London
UK                  London
Austria             Vienna
Switzerland         Bern
Germany             Berlin
France              Paris
"""

def format_capatals():
    print("%-20s%-20s" % ('Country', 'Capital'))
    print('-' * 40)
    for c in capital_country.items():
        print("%-20s%-20s" % c)

    print("{:<20}{:<20}".format('Country', 'Capital'))
    print('-' * 40)
    for c in capital_country.items():
        print("{:<20}{:<20}".format(*c))

    print("{country:<20}{capital:<20}".format(country='Country', capital='Capital'))
    print('-' * 40)
    for c in capital_country:
        print("{country:<20}{capital:<20}".format(country=c, capital=capital_country[c]))

    format_country_capital = "{country:<20}{capital:<20}".format
    print(format_country_capital(country='Country', capital='Capital'))
    print('-' * 40)
    for c in capital_country:
        print(format_country_capital(country=c, capital=capital_country[c]))


if __name__ == '__main__':
    format_capatals()