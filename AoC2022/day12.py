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

DAY = 12
PART = 1
e = get_example(DAY,0).strip()

ansExample = 29  # TO MODIFIE

# print(e)

import collections
import math
#import networkx as nx


def answer(inp="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""):
    r = 0
    bo = []
    start = None
    end = None
    for r, line in enumerate(inp.split("\n")):
        print(line)
        if "S" in line:
            start = (r, line.index("S"))
            line = line.replace("S","a")
        if "E" in line:
            end = (r, line.index("E"))
            line = line.replace("E","z")
        bo.append(line)
    m = len(line)
    n = r+1

    mini = 99**99
    for rr in range(n):
        for cc in range(m):
            if bo[rr][cc] == "a":
                queue = [(rr,cc)]
                node_in_current = 1
                node_in_next = 0
                distance = 0
                visited = [start]
                while queue:
                    r,c = queue.pop(0)
                    if (r,c) == end:
                        mini = min(mini, distance)
                        break

                    for dr,dc in (1,0),(-1,0),(0,1),(0,-1):
                        if 0<=r+dr<n and 0<=c+dc<m and (r+dr,c+dc) not in visited and ord(bo[r][c])>=ord(bo[r+dr][c+dc])-1:
                            node_in_next += 1
                            print(r,c, bo[r][c], bo[r+dr][c+dc])
                            visited.append((r+dr,c+dc))
                            queue.append((r+dr,c+dc))

                    node_in_current -= 1
                    if node_in_current == 0:
                        node_in_current = node_in_next
                        node_in_next = 0
                        distance += 1

    return mini

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



def answerPartOne(inp="""Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""):
    r = 0
    bo = []
    start = None
    end = None
    for r, line in enumerate(inp.split("\n")):
        print(line)
        if "S" in line:
            start = (r, line.index("S"))
            line = line.replace("S","a")
        if "E" in line:
            end = (r, line.index("E"))
            line = line.replace("E","z")
        bo.append(line)
    m = len(line)
    n = r+1

    queue = [start]
    node_in_current = 1
    node_in_next = 0
    distance = 0
    visited = [start]
    while queue:
        r,c = queue.pop(0)
        print(r,c)
        if (r,c) == end:
            return distance

        for dr,dc in (1,0),(-1,0),(0,1),(0,-1):
            if 0<=r+dr<n and 0<=c+dc<m and (r+dr,c+dc) not in visited and ord(bo[r][c])>=ord(bo[r+dr][c+dc])-1:
                node_in_next += 1
                print(r,c, bo[r][c], bo[r+dr][c+dc])
                visited.append((r+dr,c+dc))
                queue.append((r+dr,c+dc))

        node_in_current -= 1
        if node_in_current == 0:
            node_in_current = node_in_next
            node_in_next = 0
            distance += 1

    return r
