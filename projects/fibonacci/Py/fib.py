#!/usr/bin/env python3

import time

def fib_rec(n):
    if (n < 0):
        return 0
    if (n < 2):
        return n
    return fib_rec(n-2) + fib_rec(n-1)

def fib_lin(n):
    if (n < 0):
        return 0
    if (n < 2):
        return n
    s0 = 0
    s1 = 1
    s2 = 1
    for i in range(2, n):
        s0 = s1
        s1 = s2
        s2 = s1 + s0
    return s2

N = int(input("Enter an integer: "))

print("Recursive algorithm:")
print("{:>12} {:>12} {:>12}".format("Integer", "Fibonacci", "msecs"))
for i in range(1, N+1):
    t0 = time.time()
    f = fib_rec(i)
    t1 = time.time()
    print("{:12} {:12} {:12.6f}".format(i, f, (t1 - t0) * 1000))

print("Linear algorithm:")
print("{:>12} {:>12} {:>12}".format("Integer", "Fibonacci", "msecs"))
for i in range(1, N+1):
    t0 = time.time()
    f = fib_lin(i)
    t1 = time.time()
    print("{:12} {:12} {:12.6f}".format(i, f, (t1 - t0) * 1000))
