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

DAY = 11
PART = 2
e = get_example(DAY,0).strip()

ansExample = 2713310158  # TO MODIFIE

# print(e)

import collections
import math
#import networkx as nx

def answerEX():
    monkey = {}
    monkey[0] = {'item':[79,98],'ope':"*19",'test':(23,2,3), 'c':0}
    monkey[1] = {'item':[54,65,75,74],'ope':"+6",'test':(19,2,0),'c':0}
    monkey[2] = {'item':[79,60,97],'ope':"**2",'test':(13,1,3), 'c':0}
    monkey[3] = {'item':[74],'ope':"+3",'test':(17,0,1), 'c':0}
    divisors = [m['test'][0] for m in monkey.values()]
    modulo = math.prod(divisors)

    for i in range(10000):
        print(i)
        for m in range(len(monkey.keys())):
            while len(monkey[m]["item"])>0:
                oldLen = len(monkey[m]["item"])
                worry = monkey[m]["item"].pop(0)
                worry = eval(f"{worry}{monkey[m]['ope']}") % modulo
                if worry % monkey[m]["test"][0] == 0:
                    monkey[monkey[m]["test"][1]]["item"].append(worry)
                else:
                    monkey[monkey[m]["test"][2]]["item"].append(worry)
                monkey[m]['c'] += 1
                assert oldLen!=len(monkey[m]["item"])
    val = sorted([monkey[m]['c'] for m in range(len(monkey.keys()))])

    # print(val)
    return val[-2]*val[-1]

def answer():
    # 121800 too high
    monkey ={}
    monkey[0] = {'item':[57],'ope':"*13",'test':(11,3,2), 'c':0}
    monkey[1] = {'item':[58,93,88,81,72,73,65],'ope':"+2",'test':(7,6,7),'c':0}
    monkey[2] = {'item':[65,95],'ope':"+6",'test':(13,3,5), 'c':0}
    monkey[3] = {'item':[58,80,81,83],'ope':"**2",'test':(5,4,5), 'c':0}
    monkey[4] = {'item':[58,89,90,96,55],'ope':"+3",'test':(3,1,7), 'c':0}
    monkey[5] = {'item':[66,73,87,58,62,67],'ope':"*7",'test':(17,4,1), 'c':0}
    monkey[6] = {'item':[85,55,89],'ope':"+4",'test':(2,2,0), 'c':0}
    monkey[7] = {'item':[73,80,54,94,90,52,69,58],'ope':"+7",'test':(19,6,0), 'c':0}
    divisors = [m['test'][0] for m in monkey.values()]
    modulo = math.prod(divisors)

    # for k in monkey.keys():
    #     print(monkey[k])
    for i in range(10000):
        for m in range(len(monkey.keys())):
            while len(monkey[m]["item"]):
                monkey[m]['c'] += 1
                worry = monkey[m]["item"].pop(0) % modulo
                worry = eval(f"{worry}{monkey[m]['ope']}")
                if worry % monkey[m]["test"][0] == 0:
                    monkey[monkey[m]["test"][1]]["item"].append(worry)
                else:
                    monkey[monkey[m]["test"][2]]["item"].append(worry)
    val = sorted([monkey[m]['c'] for m in range(len(monkey.keys()))])
    return val[-2]*val[-1]

re = answerEX()
print(f"{re = }")

if re == ansExample:
    print("good answer on example")
    # s = get_input(DAY).strip()
    # print(s)

    ans = answer()
    print(ans)
    submit(DAY, PART, ans)
else:
    print("bad answer on example")




def answerPartOne():
    # 121800 too high
    monkey ={}
    monkey[0] = {'item':[57],'ope':"*13",'test':(11,3,2), 'c':0}
    monkey[1] = {'item':[58,93,88,81,72,73,65],'ope':"+2",'test':(7,6,7),'c':0}
    monkey[2] = {'item':[65,95],'ope':"+6",'test':(13,3,5), 'c':0}
    monkey[3] = {'item':[58,80,81,83],'ope':"**2",'test':(5,4,5), 'c':0}
    monkey[4] = {'item':[58,89,90,96,55],'ope':"+3",'test':(3,1,7), 'c':0}
    monkey[5] = {'item':[66,73,87,58,62,67],'ope':"*7",'test':(17,4,1), 'c':0}
    monkey[6] = {'item':[85,55,89],'ope':"+4",'test':(2,2,0), 'c':0}
    monkey[7] = {'item':[73,80,54,94,90,52,69,58],'ope':"+7",'test':(19,6,0), 'c':0}

    # for k in monkey.keys():
    #     print(monkey[k])
    for i in range(20):
        for m in range(len(monkey.keys())):
            while len(monkey[m]["item"]):
                monkey[m]['c'] += 1
                worry = monkey[m]["item"].pop(0)
                worry = eval(f"{worry}{monkey[m]['ope']}") // 3
                if worry % monkey[m]["test"][0] == 0:
                    monkey[monkey[m]["test"][1]]["item"].append(worry)
                    # print(m, monkey[m]["test"][1], worry)
                else:
                    monkey[monkey[m]["test"][2]]["item"].append(worry)
                    # print(m, monkey[m]["test"][2], worry)

    val = sorted([monkey[m]['c'] for m in range(len(monkey.keys()))])
    # print(val)
    # for k in monkey.keys():
        # print(monkey[k])
    return val[-2]*val[-1]
