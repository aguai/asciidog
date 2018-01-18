#!/usr/bin/env python3
from re import match, sub
f = sub(r"\/{4}[^\/{4}]+\/{4}|\/\/\ .+\n", '',
        open('test3.adoc').read()).splitlines()


def Blockenize(S):
    sectRe = r"(?s)\={3}\s"
    done = []
    temp = []
    while isinstance(S[0], list):
        done.append(S.pop(0))
    if match(sectRe, S[0]):
        temp.append(S.pop(0))
    while match(sectRe, S[0]) is None:
        if len(S) == 1:
            temp.append(S[0])
            S.pop(0)
            break
        else:
            temp.append(S[0])
            S.pop(0)
    done.append(temp)

    S = done + S
    if not isinstance(S[-1], list):
        Blockenize(S)
    else:
        pass
    return S



