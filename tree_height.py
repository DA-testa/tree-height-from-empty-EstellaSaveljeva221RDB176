# python3

import sys
import threading


def compute_height(n, parents):
    max_height = 0
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
    # implement input form keyboard and from files
    Print("[!] \input form keyboard and from files (capital i or capital F)")
    textInput = input(":").upper()
    
    if "F" in textInput:
        print("[!] \tEnter file name or file path. For example 'test/0'.")
        # let user input file name to use
        fileName = "test/" + input(": \t")
        # don't allow file names with letter a account for github input inprecision
        if 'a' in fileName:
            print("[Err]: \tForbidden name")
            return   
        file = open(fileName, "r")
        nodeCount = int(file.readline())
        nodes = list(map(int, file.readline().split()))
        print(compute_height(nodeCount, nodes))
        
        
    elif "I" in textInput:
        print("[!] \tEnter text below.")
        # input number of elements
        nodeCount = int(input(": \t"))
        # input values in one variable, separate with space, split these values in an array
        nodes = list(map(int, input(": ").split()))
        # call the function and output it's result
        print(compute_height(nodeCount, nodes))
    else:
        print("[Err]:\tWrong input")
    pass
        
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
