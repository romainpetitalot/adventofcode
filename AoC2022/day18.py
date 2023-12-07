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
    coordsa = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer', headers={'cookie':'session='+AOC_COOKIE}, coordsa=coordsa)
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

DAY = 18
PART = 2
e = get_example(DAY,0).strip()

ansExample = 58  # TO MODIFIE

print(e)

import collections
import math
#import networkx as nx


def answer(inp):
    coords = []
    for l in inp.split("\n"):
        coords.append( tuple(map(int, l.split(","))) )
    r = 0

    minx = min(i[0] for i in coords) - 1
    maxx = max(i[0] for i in coords) + 2
    miny = min(i[1] for i in coords) - 1
    maxy = max(i[1] for i in coords) + 2
    minz = min(i[2] for i in coords) - 1
    maxz = max(i[2] for i in coords) + 2

    water = set()
    tofill = [(minx, miny, minz)]
    while tofill:
        wx, wy, wz = tofill.pop()
        if (wx, wy, wz) in water or (wx, wy, wz) in coords:
            continue
        water.add((wx, wy, wz))
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            tx, ty, tz = wx+dx,wy+dy,wz+dz
            if minx <= tx < maxx and miny <= ty < maxy and minz <= tz < maxz:
                tofill.append((tx, ty, tz))
    for x,y,z in coords:
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            if (x+dx,y+dy,z+dz) in water:
                r += 1
    return r

re = answer(e)
print(f"{re = }")

if re == ansExample:
    print("good answer on example")
    s = get_input(DAY).strip()
    # print(s)

    ans = answer(s)
    submit(DAY, PART, ans)
else:
    print("bad answer on example")




def answerPartOne(inp):
    coords = []
    for l in inp.split("\n"):
        coords.append( tuple(map(int, l.split(","))) )
    r = len(coords * 6)

    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            a,b,c = coords[i]
            x,y,z = coords[j]
            if a==x and b==y and abs(c-z)==1:
                r -= 2
            if a==x and abs(b-y)==1 and c==z:
                r -= 2
            if abs(a-x)==1 and b==y and c==z:
                r -= 2
    return r