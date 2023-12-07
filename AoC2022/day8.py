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

DAY = 8
PART = 2
e = get_example(DAY,offset=0).strip()

ansExample = 8 # TO MODIFIE

print(e)

import collections
import math
#import networkx as nx


def answer(inp):
    res = 0
    bo = []
    for l in inp.split("\n"):
        row = list(map(int, list(l)))
        bo.append(row)

    for r in range(0, len(bo)):
        for c in range(0, len(bo[r])):
            h = bo[r][c]
            vals = []            
            for dr, dc in (1,0),(0,1),(-1,0),(0,-1):
                try:
                    i = 1
                    val = []
                    maxi = -1
                    while 0<=r+i*dr<len(bo) and 0<=c+i*dc<len(bo):
                        val.append(bo[r+i*dr][c+i*dc])
                        if bo[r+i*dr][c+i*dc] >= h:
                            break
                        i+=1
                    vals.append(len(val))
                except:
                    assert False
            assert len(vals) == 4
            if vals[0]*vals[1]*vals[2]*vals[3] > res:
                print(r,c)
                print(vals)
                res = vals[0]*vals[1]*vals[2]*vals[3]
    return res

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






# def answer(inp):
#     res = 0
#     bo = []
#     for l in inp.split("\n"):
#         row = list(map(int, list(l)))
#         bo.append(row)

#     res += 2*(len(bo) + len(bo) - 2)
#     for i in range(len(bo)):
#         print(*bo[i])
#     for r in range(1, len(bo)-1):
#         for c in range(1, len(bo[r])-1):
#             h = bo[r][c]
#             found = False
#             voisinB = [bo[nr][c] for nr in range(r+1,len(bo))]
#             if all(hh < h for hh in voisinB):
#                 print(r,c, voisinB)
#                 res += 1
#                 found = True
#             voisinH = [bo[nr][c] for nr in range(0,r)]
#             if not found and all(hh < h for hh in voisinH):
#                 print(r,c, voisinH)
#                 res += 1
#                 found = True
#             voisinL = [bo[r][nc] for nc in range(0,c)]
#             if not found and all(hh < h for hh in voisinL):
#                 print(r,c, voisinL)
#                 res += 1
#                 found = True
#             voisinR = [bo[r][nc] for nc in range(c+1,len(bo[r]))]
#             if not found and all(hh < h for hh in voisinR):
#                 print(r,c, voisinR)
#                 res += 1
#                 found = True
# 
#       return res