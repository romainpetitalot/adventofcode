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

DAY = 15
PART = 2
e = get_example(DAY,0).strip()

ansExample = 56000011  # TO MODIFIE

print(e)

import collections
import math

def manhattan(r1,c1,r2,c2):
    return abs(r1-r2) + abs(c1-c2)

def answer(inp, maxi=4000000):
    sensors = []
    beacon = {}
    for l in inp.split("\n"):
        val = l.split()
        rs, cs = map(lambda x:int(x[2:-1]), [val[2],val[3]])
        rb, cb = int(val[-2][2:-1]), int(val[-1][2:])
        sensors.append((rs,cs))
        beacon[(rs,cs)] = (rb,cb)
    x = collections.defaultdict(int)
    y = collections.defaultdict(int)
    impossible = set()
    for rs, cs in sensors:
        print(rs,cs)
        rb, cb = beacon[(rs,cs)]
        dist = manhattan(rs,cs,rb,cb)
        for nr in range(rs - dist, rs + dist+1):
            for nc in range(cs - dist, cs + dist+1):
                if manhattan(nr, nc, rs, cs) <= dist:
                    if (nr,nc) not in impossible:
                        impossible.add((nr,nc))
                        if 0<=nr<=maxi and 0<=nc<=maxi:
                            y[nr] += 1
                            x[nc] += 1

    bo = [["." for j in range(21)] for i in range(21)]

    for r in range(21):
        for c in range(21):
            if (r,c) in impossible:
                bo[r][c] = "#"

    for valX in range(0, maxi+1):
        if x[valX] == maxi:
            resX = valX

    for valY in range(0, maxi+1):
        if y[valY] == maxi:
            resY = valY

    for r in range(21):
        print(*bo[r],sep="")

    print(resX, resY)

    return resY*4000000+resX

re = answer(e, 20)
print(f"{re = }")

if re == ansExample:
    print("good answer on example")
    s = get_input(DAY).strip()
    # print(s)

    ans = answer(s)
    submit(DAY, PART, ans)
else:
    print("bad answer on example")










def answerPartOne(inp, y=2000000):
    sensors = []
    beacon = {}
    for l in inp.split("\n"):
        val = l.split()
        rs, cs = map(lambda x:int(x[2:-1]), [val[2],val[3]])
        rb, cb = int(val[-2][2:-1]), int(val[-1][2:])
        sensors.append((rs,cs))
        beacon[(rs,cs)] = (rb,cb)
    
    impossible = set()
    for rs, cs in sensors:
        print(rs,cs)
        rb, cb = beacon[(rs,cs)]
        dist = manhattan(rs,cs,rb,cb)
        for nr in range(rs - dist-1, rs + dist+2):
            nc = y
            if manhattan(nr, nc, rs, cs) <= dist:
                if (nr,nc)==(rb,cb):
                    continue
                else:
                    impossible.add((nr,nc))

    return sum([i[1]==y for i in list(impossible)])