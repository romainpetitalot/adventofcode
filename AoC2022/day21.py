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

DAY = 21
PART = 2
e = get_example(DAY,0).strip()

ansExample = 301  # TO MODIFIE

print(e)

import collections
import math
#import networkx as nx
from pprint import pformat


def answer(inp):
    r = 0
    d = {}
    ope = {}
    for l in inp.split("\n"):
        val = l.split()
        if len(val) == 2:
            if val[0] == "humn:":
                continue
            else:
                d[val[0][:-1]] = int(val[1])
        else:
            if val[0] == "root:":
                m1, m2 = val[1], val[3]
            else:
                ope[val[0][:-1]] = val[1:]


    while m1 not in d.keys() and m2 not in d.keys():
        for k, v in ope.items():
            if k not in d.keys() and v[0] in d.keys() and v[-1] in d.keys():
                d[k] = eval(f"{d[v[0]]} {v[1]} {d[v[-1]]}")        

    print(m1 in d.keys())
    print(m2 in d.keys())
    print(d[m2])

    if m2 in d.keys():
        print("m2 in d.keys()")
        newVal = {}
        val = d[m2]
        while m1 != "humn":
            newVal[m1] = val
            assert m1 not in d.keys()
            op = ope[m1]
            if op[1] == "/":
                if op[0] in d.keys():
                    val = d[op[0]] // newVal[m1]
                    m1 = op[2]
                else:
                    val = d[op[2]] * newVal[m1]
                    m1 = op[0]
            elif op[1] == "+":
                if op[0] in d.keys():
                    val = newVal[m1] - d[op[0]]
                    m1 = op[2]
                else:
                    val = newVal[m1] - d[op[2]]
                    m1 = op[0]
            elif op[1] == "-":
                if op[0] in d.keys():
                    val = d[op[0]] - newVal[m1]
                    m1 = op[2]
                else:
                    val = newVal[m1] + d[op[2]]
                    m1 = op[0]
            elif op[1] == "*":
                if op[0] in d.keys():
                    val = newVal[m1] // d[op[0]]
                    m1 = op[2]
                else:
                    val = newVal[m1] * d[op[2]]
                    m1 = op[0]


    print(format(val, 'f'))
    return val # d["root"]

re = answer(e)
print(f"{re = }")







def answerPartOne(inp):
    r = 0
    d = {}
    ope = {}
    for l in inp.split("\n"):
        val = l.split()
        if len(val) == 2:
            if val[0] == "humn:":
                d["humn"] = 82205781731577626624
            else:
                d[val[0][:-1]] = int(val[1])
        else:
            if val[0] == "root:":
                m1, m2 = val[1], val[3]
            ope[val[0][:-1]] = val[1:]


    while "root" not in d.keys():
        for k, v in ope.items():
            if k not in d.keys() and v[0] in d.keys() and v[-1] in d.keys():
                d[k] = eval(f"{d[v[0]]} {v[1]} {d[v[-1]]}")        

    print(d[m1])
    print(d[m2])
    return d["root"]







if re == ansExample:
    print("good answer on example")
    s = get_input(DAY).strip()

    ans = answerPartOne(s)
    print(ans == 82205781731577626624) # Too high
    submit(DAY, PART, ans)
else:
    print("bad answer on example")



