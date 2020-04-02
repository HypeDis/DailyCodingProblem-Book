""" 
Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds 
"""
import threading


def jobScheduler(f, n):
    timer = threading.Timer(n / 1000, f)
    timer.start()


def sayHello():
    print('hello')


jobScheduler(sayHello, 1000)
print('before or after timer?')