"""
fibonacci_recursive.py
A simple recursive function to compute the n-th Fibonacci number.
"""

def fibo (n) : 
    if n == 1 or n == 0 : 
        return n
    else : 
        return fibo(n - 1) + fibo(n - 2) 
if __name__ == "__main__" : 
    n = int(input()) 
    print ( fibo(n) ) 
