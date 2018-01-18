#!/usr/bin/env python3
from re import match, sub
f = sub(r"\/{4}[^\/{4}]+\/{4}|\/\/\ .+\n", '',
        open('resource/test2.adoc').read()).splitlines()
Begin = r'^\={3}\ '

t = []


def Blockenize(S):
    x = []
    while match(Begin, S[0]) == None:

        if len(S) == 0:
            print('no more')
            return
        elif len(S) == 1:
            x.append(S[0])
            print(S[0])
            print('______END________')
            t.append(x)
            S.pop(0)
            return
        else:
            x.append(S[0])
            print(S[0])
            S.pop(0)

    t.append(x)
    print('add a section')

    if match(Begin, S[0]):
        x.append(S[0])
        S.pop(0)
        Blockenize(S)


Blockenize(f)

for i in t:
    print("section ***********\n")
    print(i)
    print("*******************\n")
