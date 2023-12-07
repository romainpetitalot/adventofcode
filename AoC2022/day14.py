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

def ints(s, ):
    return list(map(int, s.split()))

DAY = 14
PART = 2
e = get_example(DAY,0).strip()

ansExample = 93  # TO MODIFIE

# print(e)

import collections
import math
#import networkx as nx


def answer(inp="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""):

    res = 0
    coords = set()
    maxR = 0
    for l in inp.split("\n"):
        # print(l.split(" -> "))
        val = list( map(lambda x:tuple(map(int, x.split(","))), l.split(" -> ")) ) 
        for p1, p2 in zip(val, val[1:]):
            c1, r1 = p1
            c2, r2 = p2
            maxR = max(maxR, r1, r2)
            if c1 == c2:
                assert r1!=r2
                for rr in range(min(r1,r2), max(r1,r2)+1):
                    coords.add((rr,c1))
            else:
                for cc in range(min(c1,c2), max(c1,c2)+1):
                    coords.add((r1,cc))
    for cc in range(-10000, 10000):
        coords.add((maxR+2, cc))
    
    print(len(coords))
    sortiDeLaMap = False
    while not sortiDeLaMap:
        stop = False
        r,c = 0,500
        while not stop:
            if (r+1, c) not in coords:
                r += 1
            elif (r+1, c-1) not in coords:
                r += 1
                c -= 1
            elif (r+1, c+1) not in coords:
                r += 1
                c += 1
            else:
                stop = True
                assert (r,c) not in coords
                coords.add((r,c))
                res += 1
                if (r,c) == (0,500):
                    sortiDeLaMap = True

    return res

re = answer()
print(f"{re = }")

if re == ansExample:
    print("good answer on example")
    s = get_input(DAY).strip()
    # print(s)

    ans = answer(s)
    submit(DAY, PART, ans)
else:
    print("bad answer on example")




def answerPartOne(inp="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""):

    res = 0
    coords = set()
    maxR = 0
    for l in inp.split("\n"):
        # print(l.split(" -> "))
        val = list( map(lambda x:tuple(map(int, x.split(","))), l.split(" -> ")) ) 
        for p1, p2 in zip(val, val[1:]):
            c1, r1 = p1
            c2, r2 = p2
            maxR = max(maxR, r1, r2)
            if c1 == c2:
                assert r1!=r2
                for rr in range(min(r1,r2), max(r1,r2)+1):
                    coords.add((rr,c1))
            else:
                for cc in range(min(c1,c2), max(c1,c2)+1):
                    coords.add((r1,cc))
    
    print(len(coords))
    print(list(coords))
    sortiDeLaMap = False
    while not sortiDeLaMap:
        stop = False
        r,c = 0,500
        while not stop:
            if r > maxR:
                stop = True
                sortiDeLaMap = True
            else:
                if (r+1, c) not in coords:
                    r += 1
                elif (r+1, c-1) not in coords:
                    r += 1
                    c -= 1
                elif (r+1, c+1) not in coords:
                    r += 1
                    c += 1
                else:
                    stop = True
                    assert (r,c) not in coords
                    coords.add((r,c))
                    res += 1

    return res