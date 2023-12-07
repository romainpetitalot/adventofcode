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

DAY = 7
PART = 2
e = get_example(DAY,1).strip()

ansExample = 24933642  # TO MODIFIE

print(e)

import collections
import math
#import networkx as nx


def answer(inp):
    r = 0
    ssdos = collections.defaultdict(list)
    file = collections.defaultdict(int)
    currentdos = ["/"]
    showFile = False
    i = 0
    show = set()
    for l in inp.split("\n"):
        assert currentdos[0] == "/"
        cmd = l.split()
        if i==0:
            i+=1
            continue
        print(cmd)
        if showFile:
            if cmd[0] == "$":
                i+=1
                showFile = False
                assert cmd[1] == "cd"
                if cmd[2]=="..":
                    currentdos.pop(-1)
                elif cmd[2] in ssdos[tuple(currentdos)]:
                    currentdos.append(cmd[2])
                else:
                    print("probelem1")
                    assert False
            elif cmd[0] == "dir":
                ssdos[tuple(currentdos)].append(cmd[1])
            else:
                for i in range(1,len(currentdos)+1):
                    file[tuple(currentdos[:i])] += int(cmd[0])

        else:
            i+=1
            if cmd[1] == "ls":
                showFile = True
                # assert currentdos[-1] not in show
                # show.add(currentdos[-1])
            elif cmd[1] == "cd":
                if cmd[2]=="..":
                    currentdos.pop(-1)
                elif cmd[2] in ssdos[tuple(currentdos)]:
                    currentdos.append(cmd[2])
                else:
                    print("probelem2")
                    assert False
            else:
                assert False
    print(file)
    print(ssdos)
    print(i)
    res = [t for t in file.items()]
    res.sort(key=lambda x:x[1])
    print(res)
    total = file[('/',)]
    diffInf = 70000000 - total
    print(diffInf)
    print(total)
    for t in res:
        if len(t[0])<=2:
            print(t)
        if t[1] >= 30000000 - diffInf:
            return t[1]
    # for k, v in file.items():
        # if v <= 100000:
            # r += v
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

