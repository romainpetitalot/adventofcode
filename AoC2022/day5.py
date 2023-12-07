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

DAY = 5
PART = 2
e = "    "+get_example(DAY).strip()

ansExample = "MCD"  # TO MODIFIE

print(e)

import collections
import math
#import networkx as nx


def answer(inp, nb = 9):
    r = ""
    dico = collections.defaultdict(list)
    for l in inp.split("\n"):
        print(l)
        if len(l) == 0:
            print(dico)
            continue
        elif l[0] == "m":
            z, n, y, a, x, b = l.split()
            n, a, b = map(int, [n,a,b])
            new = []
            for i in range(n):
                new.append( dico[a].pop(0))
            dico[b] = new + dico[b]
            print(n,a,b)
            print(dico)
            
        else:
            count = 1
            for i in range(1, 1+4*(nb), 4):
                try:
                    if l[i] == "1":
                        # toContinue = True
                        break
                    elif l[i] != " ":
                        dico[count].append( l[i] )
                    count += 1
                except:
                    break
    for i in range(nb):
        r+=dico[i+1][0]
    return r

re = answer(e, 3)
print(f"{re = }")

if re == ansExample:
    print("good answer on example")
    s = "    "+get_input(DAY).strip()

    print(s)


    ans = answer(s)

    submit(DAY, PART, ans)
else:
    print("bad answer on example")