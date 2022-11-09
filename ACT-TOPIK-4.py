No.1

from linkedliststack import Stack

def transferStack(stackSumber, stackTujuan):
    while not stackSumber.isEmpty():
        nilai = stackSumber.pop()
        stackTujuan.push(nilai)
    if stackTujuan.isEmpty() != 0:
        print("stackB tidak kosong.")
        
==============

No.2

from linkedliststack import Stack

def transferStack(stackSumber, stackTujuan):
    while not stackSumber.isEmpty():
        nilai = stackSumber.pop()
        stackTujuan.push(nilai)
    if stackTujuan.isEmpty() != 0:
        print("stackB tidak kosong.")
