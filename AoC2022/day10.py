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

DAY = 10
PART = 1

e = get_example(DAY,1).strip()

ansExample = 1  # TO MODIFIE

# print(e)

import collections
import math
#import networkx as nx


def answer(inp):
    r = ""
    x = 1
    cycle = 0
    for l in inp.split("\n"):
        if l == "noop":
            if abs(x-cycle%40)<=1:
                r+="#"
            else:
                r+="."   
            cycle += 1
        else:
            if abs(x-cycle%40)<=1:
                r+="#"
            else:
                r+="."
            cycle += 1

            if abs(x-cycle%40)<=1:
                r+="#"
            else:
                r+="."
            cycle += 1

            a, val = l.split()
            x += int(val)    


    return r

re = answer(e)
# print(f"{re = }")

for i in range(6):
    print(re[40*i:40*(i+1)])
re = 1


if re == ansExample:
    print("good answer on example")
    s = get_input(DAY).strip()
    # print(s)

    ans = answer(s)
    for i in range(6):
        print(ans[40*i:40*(i+1)])
    submit(DAY, PART, ans)
else:
    print("bad answer on example")







def answerPartOne(inp):
    r = 0
    x = 1
    cycle = 0
    for l in inp.split("\n"):
        if l == "noop":
            if cycle in [20,60,100,140,180,220]:
                print(x)
                r +=  cycle*x
            cycle += 1
            
        else:
            if cycle in [20,60,100,140,180,220]:
                print(x)
                r +=  cycle*x
            cycle += 1
            if cycle in [20,60,100,140,180,220]:
                print(x,'obled')
                r += cycle*x    
            cycle += 1

            a, val = l.split()
            x += int(val)    


    return r # Ne marchait pas avec l'exemple mais marchait pour l'input part 1