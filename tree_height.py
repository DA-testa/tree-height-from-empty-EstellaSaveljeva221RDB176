# python3

import sys
import threading


def compute_height(n, parents):
    max_height = [0] * n
    for i in range(n):
        node = i
        h = 0
        while node != -1:
            if max_height[node] != 0:
                h += max_height[node]
                break
            h += 1
            node = parents[node]
        max_height[i] = h
    return max_height


def main():
    Print("[!] \input form keyboard and from files (capital i or capital F)")
    textInput = input(":").upper()
    
    if "F" in textInput:
        print("[!] \tEnter file name or file path. For example 'test/0'.")
        fileName = "test/" + input(": \t")
        if 'a' in fileName:
            print("[Err]: \tForbidden name")
            return   
        file = open(fileName, "r")
        nodeCount = int(file.readline())
        nodes = list(map(int, file.readline().split()))
        print(compute_height(nodeCount, nodes))
        
        
    elif "I" in textInput:
        print("[!] \tEnter text below.")
        nodeCount = int(input(": \t"))
        nodes = list(map(int, input(": ").split()))
        print(compute_height(nodeCount, nodes))
    else:
        print("[Err]:\tWrong input")
    pass
        

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
