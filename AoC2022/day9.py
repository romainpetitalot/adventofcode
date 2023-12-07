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

DAY = 9
PART = 2
e = get_example(DAY, 7).strip()

ansExample = 36  # TO MODIFIE

print(e)

import collections
import math
#import networkx as nx


def answer(inp):
    direction = {'R':(1,0),'L':(-1,0),'D':(0,-1),'U':(0,1)}
    nodes = {}
    for i in range(10):
        nodes[i] = (0,0)
    memo = set()
    memo.add((0,0))
    r = 0
    li = []
    for l in inp.split("\n"):
        _dir, val = l.split()
        val = int(val)
        dx, dy = direction[_dir]

        for i in range(val):
            print(nodes[0], _dir)
            print()
            for ind in range(9):
                hx, hy = nodes[ind]
                tx, ty = nodes[ind+1]
                if ind == 0:
                    hx += dx
                    hy += dy
                isVoisin = False
                for dxx in range(-1,2):
                    for dyy in range(-1,2):
                        if hx+dxx == tx and hy+dyy == ty:
                            isVoisin = True
                            break
                if not isVoisin:
                    if tx<hx:
                        tx+=1
                    elif tx>hx:
                        tx-=1
                    if ty<hy:
                        ty+=1
                    elif ty>hy:
                        ty-=1
                    isVoisin = False
                    for dxx in range(-1,2):
                        for dyy in range(-1,2):
                            if hx+dxx == tx and hy+dyy == ty:
                                isVoisin = True
                                break
                    assert isVoisin
                    if ind==8:
                        memo.add((tx,ty))
                nodes[ind]=(hx,hy)
                nodes[ind+1]=(tx,ty)
    print(memo)
    return len(memo)
    # Doit être plus petit que 5684 c'est 5683 mais je sais pas pk
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




def answerPart1(inp):
    direction = {'R':(1,0),'L':(-1,0),'D':(0,-1),'U':(0,1)}
    hx, hy = 0, 0
    tx, ty = 0, 0
    memo = set((0,0))
    r = 0
    li = []
    for l in inp.split("\n"):
        _dir, val = l.split()
        val = int(val)
        for i in range(val):
            dx, dy = direction[_dir]
            print()
            print(_dir,i)
            print((hx,hy),(tx,ty))
            hx += dx
            hy += dy
            isVoisin = False
            for dxx in range(-1,2):
                for dyy in range(-1,2):
                    if hx+dxx == tx and hy+dyy == ty:
                        isVoisin = True
                        break
            if not isVoisin:
                if tx<hx:
                    tx+=1
                elif tx>hx:
                    tx-=1
                if ty<hy:
                    ty+=1
                elif ty>hy:
                    ty-=1
                isVoisin = False
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if hx+dx == tx and hy+dy == ty:
                            isVoisin = True
                            break
                assert isVoisin
                li.append((tx,ty))
                memo.add((tx,ty))
    print(li)
    return len(memo)
    # Doit être plus petit que 5684 c'est 5683 mais je sais pas pk