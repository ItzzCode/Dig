#imports
from time import sleep
from os import system
from termcolor import cprint
#esolangs.org/wiki/Dig
def clear():
    system("clear")
line = ""
#input stuff
while True:
    line += input("") + "\n"
    clear()
    print(line)
    done = input("Finished? (y/n)")
    if done == "y":
break
clear()
#make the code into 2d list
line = list(line) n=0
#loop through to find \n
for i in range(len(line)):
    if line[i] == "\n":
        n += 1
#making list
scode = list(" " * n)
b=0
s=0
for i in range(len(line)):
    if s > len(scode):
        break
if line[i] == "\n": scode[s] = line[b:i] b=i+1
s += 1

#thanks samwise! your answer on stack overflow was short but usable
for a in scode:
    a.extend([" "] * (max(map(len, scode)) - len(a)))
direction = 0
cords = [0, 0]
memory = 0
tmem = list(" " * 30)
vchar = [
    ["^", ">", "'", "<", "$", "#", "@"],
    [
"=", "~", ":", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNLOPQRSTUVWXY.,?!Z1234567890"
,
"+", "-", "*", "/", ";", "%"
] ]
errors = [
    "Interpretor Error: More than one number next to command",
    "Error: Division by 0",
    "Error: Invalid character",
    "Interpretor Error: Tile memory full",
    "User Error: Manually halted"
]
def move(x, y, d):
    if d in {1, 3}:
if d == 1: y+=1
else: y-=1
    if d in {2, 4}:
        if d == 2:
x+=1 else:
x-=1 return x, y
def execute(char, mem):
    if char in vcar[0]:
