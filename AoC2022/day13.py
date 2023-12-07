# Advent of Code template by @MathisHammel

import requests

from aoc_secrets import AOC_COOKIE # Put your session cookie in this variable
YEAR = '2022'

def get_input(day):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input', headers={'cookie':'session='+AOC_COOKIE})
    return req.text

def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}', headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]

def submit(day, level, answer):
    input(f'You are about to submit the follwing answer:\n>>>>>>>>>>>>>>>>> {answer}\nPress enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer', headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        print('VERDICT : INVALID LEVEL')
    else:
        print('VERDICT : OK !')

def ints(s):
    return list(map(int, s.split()))

DAY = 13
PART = 2
e = get_example(DAY,0).strip()

ansExample = 140  # TO MODIFIE

# print(e)

import collections
import math
#import networkx as nx

def compare(l1, l2):
    if isinstance(l1, int):
        if isinstance(l2, int):
            if l1<l2:
                return -1
            elif l2<l1:
                return 1
        else:
            tmp = [l1]
            return isGoodOrder(tmp, l2)
    else:
        if isinstance(l2, list):
            return isGoodOrder(l1, l2)
        else:
            tmp = [l2]
            return isGoodOrder(l1, tmp)


        if len(l1) == 0:
            assert len(l2) > 0
            return -1
        if len(l2) == 0:
            return 1

def isGoodOrder(l1, l2):
    res = None
    for val1, val2 in zip(l1, l2):
        val = compare(val1, val2)
        if val is not None:
            return val
    if len(l1) < len(l2):
        return -1
    if len(l1) > len(l2):
        return 1

import functools

def answer(inp):
    r = 0
    inp = inp.splitlines()
    a = [[2]]
    b = [[6]]
    l = [ a, b ]
    for i in range(0,len(inp), 3):
        l1 = eval(inp[i])
        l2 = eval(inp[i+1])
        l.append(l1)
        l.append(l2)

    l = sorted(l ,key=functools.cmp_to_key(isGoodOrder))
    # print(*l, sep="\n")
    return (l.index(a)+1) * (l.index(b)+1)

    new = [1] # On initialise avec une premiere valeur à l'interieur car on veut que l'index soit 1-indexed
    n = len(l)
    while len(new) < n:
        for i, l1 in enumerate(l):
            if all( isGoodOrder(l1,l2)==-1 for l2 in l if l2 not in new and l1!=l2 ):
                new.append(l1)
                l.pop(i)
                break
    # print(*new, sep="\n")
    return new.index(a) * new.index(b)

re = answer(e)
print(f"{re = }")
import time
if re == ansExample:
    print("good answer on example")
    s = get_input(DAY).strip()
    # print(s)
    s0 = time.time()
    ans = answer(s)
    print(time.time()-s0)
    submit(DAY, PART, ans)
else:
    print("bad answer on example")

def answerPartOne(inp):
    r = 0
    inp = inp.splitlines()
    for i in range(0,len(inp), 3):
        l1 = eval(inp[i])
        l2 = eval(inp[i+1])
        if isGoodOrder(l1, l2) == -1:
            r += i//3 + 1
            print(l1, l2)
            print(f"{r = }")

    return r